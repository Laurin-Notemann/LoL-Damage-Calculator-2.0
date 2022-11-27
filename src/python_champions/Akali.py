from Champion.Champion import Champion
from ChampionAbility.Ability import Ability
from ChampionAbility.Damage import Damage
from ChampionAbility.DamageType import DamageType
from ChampionAbility.MissingHealthData import MissingHealthData


class Akali(Champion):

    def __init__(self, champ_dict: dict):
        super().__init__(champ_dict)
        self.has_assassins_mark: bool = False
        self.missing_health_damage_amplifier: float = 0.0286
        self.per_missing_health_percentage: float = 0.01
        self.missing_health_cap: float = 0.7

    def set_assissins_mark_true(self):
        self.has_assassins_mark = True

    def auto_attack(self):
        damage_auto_attack: Damage = Damage(DamageType.PHYSICAL)
        damage_auto_attack.set_damage(self.total_attack_damage)
        if self.has_assassins_mark:
            damage_passive: Damage = self.passive_action()
            self.has_assassins_mark = False
            return [damage_auto_attack, damage_passive]
        else:
            return damage_auto_attack

    def passive_action(self):
        damage: Damage = Damage(DamageType.MAGIC)
        ad_amp: float = self.bonus_attack_damage * 0.6
        ap_amp: float = self.total_ability_power_flat * 0.55
        passive_base_damage: float = 35

        # starting at 2 because 35 is for level 1 and then in goes through all the level
        for i in range(2, 19):
            if i <= self.champion_level and i <= 6:
                passive_base_damage += 3
            elif i <= self.champion_level and 7 <= i <= 12:
                passive_base_damage += 9
            elif self.champion_level >= i >= 13:
                passive_base_damage += 15
        damage.set_damage(passive_base_damage + ad_amp + ap_amp)
        return damage

    def q_action(self, skill_level: int = -1):
        q: Ability = self.ability_q[0]
        if self.skill_level_inside_bounds(skill_level, q):
            self.set_assissins_mark_true()
            return q.get_damage(skill_level, 0)

    def w_action(self, skill_level: int = -1):
        return None

    def e_action(self, skill_level: int = -1, first_instance: bool = True, second_instance: bool = True):
        e: Ability = self.ability_e[0]
        if skill_level > -1:
            # technically works for both instances not implemented yet
            self.set_assissins_mark_true()
            if second_instance:
                return e.get_damage(skill_level, 2, 1)
            return e.get_damage(skill_level, 0)

    def r_action(self, skill_level: int = -1, enemy_current_hp: float = 0, first_instance: bool = True, second_instance: bool = True):
        r: Ability = self.ability_r[0]
        if self.skill_level_inside_bounds(skill_level, r):
            # technically works for both instances not implemented yet
            self.set_assissins_mark_true()

            missing_health: MissingHealthData = MissingHealthData(
                self.enemy_health, 
                enemy_current_hp, 
                self.missing_health_damage_amplifier, 
                self.per_missing_health_percentage, 
                self.missing_health_cap
            )

            damage_first_r: Damage = r.get_damage(skill_level, 0)
            damage_second_r: Damage = r.get_damage_based_on_enemy_health(skill_level, 2, missing_health)
            damage_total: list[Damage] = [damage_first_r, damage_second_r]

            if first_instance and second_instance:
                return damage_total
            elif first_instance:
                return damage_first_r
            elif second_instance:
                return damage_second_r

    def __getstate__(self):
        state = self.__dict__.copy()
        del state["champ_dict"]
        del state["stats"]
        del state["item_dict"]
        del state["has_assassins_mark"]
        return state

    def __setstate__(self, state):
        self.__dict__.update(state)
