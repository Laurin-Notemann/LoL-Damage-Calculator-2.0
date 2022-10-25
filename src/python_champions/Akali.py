from Champion import Champion
from get_dict import get_dict


class Akali(Champion):

    def __init__(self, champ_dicdt):
        super().__init__(champ_dicdt)
        self.has_assassins_mark = False

    def auto_attack(self):
        if self.has_assassins_mark:
            return ["MIXED_DAMAGE", [self.base_attack_damage], ]
            pass

    def passive_ability(self):
        attack_damage_amp = self.bonus_attack_damage * 0.6
        ability_power_amp = self.ability_power_flat * 0.55
        passive_damage = 35

        for i in range(2, 19):
            if i <= self.champion_level and i <= 6:
                passive_damage += 3
            elif i <= self.champion_level and 7 <= i <= 12:
                passive_damage += 9
            elif i <= self.champion_level and 13 <= i:
                passive_damage += 15

        return ["MAGIC_DAMAGE", passive_damage + attack_damage_amp + ability_power_amp]


def q_ability(self, skill_level=-1):
    pass


def w_ability(self, skill_level=-1):
    pass


def e_ability(self, skill_level=-1):
    pass


def r_ability(self, skill_level=-1):
    pass


akali = Akali(get_dict("Akali"))
