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
        for i in range(1, 19):
            # 0.0041 is a specfic amount provided by league of legends
            perc_amp += 0.0041
            if self.champion_level == i:
                damage.set_damage(perc_amp*self.enemy_health)
                return damage

    def q_action(self, skill_level=-1, is_sweet_spot=False, time_casted=0):
        key = "Q"
        q = self.ability_q[0]
        if skill_level > -1:
            for i in range(0, 3):
                if i == time_casted:
                    if is_sweet_spot:
                        return q.get_damage(skill_level, i+2, 1)
                    return q.get_damage(skill_level, i+2, 0)

    def w_action(self, skill_level=-1, tether_completed=True):
        key = "W"
        if skill_level > -1:
            if tether_completed:
                return self.wrapper_for_dmg(key, skill_level, 2, 0, "AD")
            return self.wrapper_for_dmg(key, skill_level, 0, 0, "AD")

    def e_action(self, skill_level=-1):
        return None

    def r_action(self, skill_level=-1):
        key = "R"
        ability_value_dict = self.get_ability_values(key)[key][0]

        if skill_level > -1:
            self.bonus_attack_damage += self.total_attack_damage * \
                (1 + (ability_value_dict["effect2"]
                 ["attribute0"][0][0][skill_level] / 100))
            # needs to be called everytime bonus AD changes
            self.set_base_stats_based_on_level()

    def __getstate__(self):
        state = self.__dict__.copy()
        del state["champ_dict"]
        del state["stats"]
        del state["item_dict"]
        del state["has_passive"]
        return state

    def __setstate__(self, state):
        self.__dict__.update(state)
