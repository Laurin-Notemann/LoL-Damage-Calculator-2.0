from python_champions.Champion import Champion


class Akali(Champion):

    def __init__(self, champ_dict):
        super().__init__(champ_dict)
        self.has_assassins_mark = False
        #  self.total_ability_power_flat = 50

    def auto_attack(self):
        if self.has_assassins_mark:
            self.has_assassins_mark = False
            return ["MIXED_DAMAGE", ["PHYSICAL_DAMAGE", self.total_attack_damage], ["MAGIC_DAMAGE", self.passive_ability()]]
        else:
            return ["PHYSICAL_DAMAGE", self.total_attack_damage, None]

    def passive_ability(self):
        attack_damage_amp = self.bonus_attack_damage * 0.6
        ability_power_amp = self.total_ability_power_flat * 0.55
        passive_damage = 35

        for i in range(2, 19):
            if i <= self.champion_level and i <= 6:
                passive_damage += 3
            elif i <= self.champion_level and 7 <= i <= 12:
                passive_damage += 9
            elif self.champion_level >= i >= 13:
                passive_damage += 15
        return ["MAGIC_DAMAGE", passive_damage + attack_damage_amp + ability_power_amp]

    def q_ability(self, skill_level=-1):
        key = "Q"

        if skill_level > -1:
            self.has_assassins_mark = True
            return self.wrapper_for_dmg(key, skill_level, 0, 0, "AD", "AP")

    def w_ability(self, skill_level=-1):
        return None

    def e_ability(self, skill_level=-1, first_instance=True, second_instance=True):
        key = "E"

        if skill_level > -1:
            self.has_assassins_mark = True  # technically works for both instances not implemented yet
            if second_instance:
                return self.wrapper_for_dmg(key, skill_level, 2, 1, "AD", "AP")
            return self.wrapper_for_dmg(key, skill_level, 0, 0, "AD", "AP")

    def r_ability(self, skill_level=-1, enemy_current_hp=0, first_instance=True, second_instance=True):
        key = "R"

        if skill_level > -1:
            self.has_assassins_mark = True  # technically works for both instances not implemented yet

            enemy_missing_health_perc = self.get_missing_health(self.enemy_health, enemy_current_hp)
            damage_amp = self.get_amp_based_on_missing_health(enemy_missing_health_perc, 0.01, 0.0286, 0.7)

            damage_first_r = self.wrapper_for_dmg(key, skill_level, 0, 0, "BONUS_AD", "AP")
            damage_second_r_without_amp = self.wrapper_for_dmg(key, skill_level, 2, 0, "AP")
            damage_second_r_with_amp = round(damage_second_r_without_amp[1] + (damage_second_r_without_amp[1] * damage_amp), 3)
            damage_second_r = [damage_second_r_without_amp[0], damage_second_r_with_amp, None]

            damage_total = ["MAGIC_DAMAGE", damage_first_r[1] + damage_second_r[1], None]

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
