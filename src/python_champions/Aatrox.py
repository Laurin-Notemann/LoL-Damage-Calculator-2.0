from Champion.Champion import Champion
from ChampionAbility.Ability import Ability
from ChampionAbility.Damage import Damage
from ChampionAbility.DamageType import DamageType


class Aatrox(Champion):

    def __init__(self, champ_dict):
        super().__init__(champ_dict)
        self.has_passive = True

    def auto_attack(self):
        damage_auto_attack: Damage = Damage(DamageType.PHYSICAL)
        damage_auto_attack.set_damage(self.total_attack_damage)
        if self.has_passive:
            passive_damage: Damage = self.passive_ability()
            return [damage_auto_attack, passive_damage]
        else:
            return damage_auto_attack

    def passive_ability(self):
        damage: Damage = Damage(DamageType.PHYSICAL)

        perc_amp = 0.0459
        # for loop goes through all the levels 1-18
        for i in range(1, 19):
            # 0.0041 is a specfic amount provided by league of legends
            perc_amp += 0.0041
            if self.champion_level == i:
                damage.set_damage(perc_amp*self.enemy_health)
                return damage

    def q_action(self, skill_level: int=-1, is_sweet_spot: bool=False, time_casted: int=0):
        q: Ability = self.ability_q[0]
        if self.skill_level_inside_bounds(skill_level, q):
            # Aatrox has three different cast, that all deal different amount of damage the loop finds which cast was input
            for i in range(0, 3):
                if i == time_casted:
                    if is_sweet_spot:
                        return q.get_damage(skill_level, i + 2, 1)
                    return q.get_damage(skill_level, i + 2, 0)

    def w_action(self, skill_level: int=-1, tether_completed: bool=True):
        w: Ability = self.ability_w[0]
        if self.skill_level_inside_bounds(skill_level, w):
            if tether_completed:
                return w.get_damage(skill_level, 2)
            return w.get_damage(skill_level, 0)

    def e_action(self, skill_level: int=-1):
        return None

    def r_action(self, skill_level: int=-1):
        r: Ability = self.ability_r[0]
        if self.skill_level_inside_bounds(skill_level, r):
            r_ad: float = r.effects[0].attributes[0][0].values[skill_level]
            bonus_ad_from_r: float = self.total_attack_damage * (1 + (r_ad / 100))
            self.bonus_attack_damage += bonus_ad_from_r
            # needs to be called everytime bonus AD changes
            self.set_total_value_to_based_on_level_and_item_stats()

    def __getstate__(self):
        state = self.__dict__.copy()
        del state["champ_dict"]
        del state["stats"]
        del state["item_dict"]
        del state["has_passive"]
        return state

    def __setstate__(self, state):
        self.__dict__.update(state)
