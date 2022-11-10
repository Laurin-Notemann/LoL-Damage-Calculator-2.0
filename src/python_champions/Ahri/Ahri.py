from python_champions.Champion import Champion
from python_champions.get_dict import get_dict


class Ahri(Champion):
    def __init__(self, champ_dict):
        super().__init__(champ_dict)
        self.total_ability_power_flat = 0

    def passive_ability(self):
        pass

    def q_ability(self, skill_level=-1, first_pass=True, last_pass=True):
        key = "Q"

        if skill_level > -1:
            if first_pass and last_pass:
                return ["MIXED_DAMAGE",
                        ["MAGIC_DAMAGE", self.wrapper_for_dmg(key, skill_level, 0, 0, "AP")[1]],
                        ["TRUE_DAMAGE", self.wrapper_for_dmg(key, skill_level, 0, 0, "AP")[1]]]
            elif first_pass:
                return ["MAGIC_DAMAGE", self.wrapper_for_dmg(key, skill_level, 0, 0, "AP")[1], None]
            elif last_pass:
                return ["TRUE_DAMAGE", self.wrapper_for_dmg(key, skill_level, 0, 0, "AP")[1], None]

    def w_ability(self, skill_level=-1, amount_hit=3):
        key = "W"

        if skill_level > -1:
            if amount_hit == 1:
                return self.wrapper_for_dmg(key, skill_level, 1, 0, "AP")
            elif amount_hit == 2:
                first_hit = self.wrapper_for_dmg(key, skill_level, 1, 0, "AP")[1]
                second_hit = self.wrapper_for_dmg(key, skill_level, 2, 0, "AP")[1]
                return ["MAGIC_DAMAGE", first_hit + second_hit, None]
            elif amount_hit == 3:
                return self.wrapper_for_dmg(key, skill_level, 2, 1, "AP")

    def e_ability(self, skill_level=-1):
        key = "E"

        if skill_level > -1:
            return self.wrapper_for_dmg(key, skill_level, 0, 0, "AP")

    def r_ability(self, skill_level=-1, amount_used=1):
        key = "R"

        if skill_level > -1:
            return [self.wrapper_for_dmg(key, skill_level, 0, 0, "AP")[0], self.wrapper_for_dmg(key, skill_level, 0, 0, "AP")[1] * amount_used, None]


# ahri = Ahri(get_dict("Ahri"))
"""
print(ahri.auto_attack())
print(ahri.q_ability(0))
print(ahri.w_ability(1))
print(ahri.e_ability(1))
print(ahri.r_ability(1))
"""