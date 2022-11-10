from python_champions.Champion import Champion
from python_champions.get_dict import get_dict


class Seraphine(Champion):

    def __init__(self, champ_dict, enemy_max_hp):
        """ Seraphine init:
        echo: increases by 1 everytime she uses an ability, when echo = 3 an ability will be performed twice and set echo = 0
        note_stacks: increases by 1 everytime she uses an ability, max is 4, when she AA she consumes then and deals damage and set note_stacks = 0

        """
        super().__init__(champ_dict)
        self.echo = 0
        self.note_stacks = 0
        self.enemy_max_hp = enemy_max_hp
        self.total_ability_power_flat = 30  # just for testing not for final

        # self.is_echo = False

    def check_echo(self):
        if self.echo == 3:
            return True
        return False

    def auto_attack(self):
        if self.note_stacks == 0:
            damage_type = "PHYSICAL_DAMAGE"
            return [damage_type, self.total_attack_damage, None]  # see explanation at wrapper_func
        else:
            damage_type = "MIXED_DAMAGE"
            return [damage_type, ["PHYSICAL_DAMAGE", self.total_attack_damage], self.passive_ability()]

    # returns value of the additional damage (only works for the notes she creates by herself so max is 4 currently)
    def passive_ability(self):
        damage_type = self.passive_ability_dict["damage_type"]
        damage = []

        ap_amplifier_based_on_ability_scaling = self.total_ability_power_flat * 0.07

        if self.note_stacks > 4:
            self.note_stacks = 4

        if self.champion_level < 6:
            damage = [damage_type, round((4 + ap_amplifier_based_on_ability_scaling) * self.note_stacks, 2), None]
        elif self.champion_level < 11:
            damage = [damage_type, round((8 + ap_amplifier_based_on_ability_scaling) * self.note_stacks, 2), None]
        elif self.champion_level < 16:
            damage = [damage_type, round((14 + ap_amplifier_based_on_ability_scaling) * self.note_stacks, 2), None]
        elif self.champion_level < 19:
            damage = [damage_type, round((24 + ap_amplifier_based_on_ability_scaling) * self.note_stacks, 2), None]

        self.note_stacks = 0
        return damage

    def q_ability(self, enemy_current_hp=0, skill_level=-1):
        """ Seraphine Q-Ability "High Note"
        Important
        """
        key = "Q"

        if skill_level > -1:
            self.note_stacks += 1

            enemy_missing_health_perc = self.get_missing_health(self.enemy_max_hp, enemy_current_hp)

            damage_amplifier_missing_health = self.get_amp_based_on_missing_health(enemy_missing_health_perc, 0.0003, 0.0002, 0.75)

            damage_total_without_amp = self.wrapper_for_dmg(key, skill_level, 0, 0, "AP")
            damage_total_with_amp = damage_total_without_amp[1] + (damage_total_without_amp[1] * damage_amplifier_missing_health)

            return [damage_total_without_amp[0], damage_total_with_amp, None]

    def w_ability(self, skill_level=-1):
        return None

    def e_ability(self, skill_level=-1):
        key = "E"

        if skill_level > -1:
            self.note_stacks += 1
            return self.wrapper_for_dmg(key, skill_level, 0, 0, "AP")

    def r_ability(self, skill_level=-1):
        key = "R"

        if skill_level > -1:
            self.note_stacks += 1
            return self.wrapper_for_dmg(key, skill_level, 0, 0, "AP")


sera = Seraphine(get_dict("Seraphine"), 1000)
# print(vars(sera))
"""
print(sera.q_ability(250, 3))
print(sera.w_ability(2))
print(sera.e_ability(2))
print(sera.r_ability(2))
print(sera.auto_attack())
print(sera.passive_ability())
"""