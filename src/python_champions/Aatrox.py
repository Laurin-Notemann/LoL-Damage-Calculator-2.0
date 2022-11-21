from Champion.Champion import Champion


class Aatrox(Champion):

    def __init__(self, champ_dict):
        super().__init__(champ_dict)
        self.has_passive = True

    def auto_attack(self):
        if self.has_passive:
            return ["PHYSICAL_DAMAGE", self.total_attack_damage + self.passive_ability()[1], None]
        else:
            return ["PHYSICAL_DAMAGE", self.total_attack_damage, None]

    def passive_ability(self):
        damage_type = "PHYSICAL_DAMAGE"

        perc_amp = 0.0459

        for i in range(1, 19):
            perc_amp += 0.0041
            if self.champion_level == i:
                return [damage_type, perc_amp * self.enemy_health, None]

    def q_ability(self, skill_level=-1, is_sweet_spot=False, time_casted=0):
        key = "Q"

        if skill_level > -1:
            for i in range(0, 3):
                if i == time_casted:
                    if is_sweet_spot:
                        return self.wrapper_for_dmg(key, skill_level, i + 2, 1, "AD")
                    return self.wrapper_for_dmg(key, skill_level, i + 2, 0, "AD")

    def w_ability(self, skill_level=-1, tether_completed=True):
        key = "W"
        if skill_level > -1:
            if tether_completed:
                return self.wrapper_for_dmg(key, skill_level, 2, 0, "AD")
            return self.wrapper_for_dmg(key, skill_level, 0, 0, "AD")

    def e_ability(self, skill_level=-1):
        return None

    def r_ability(self, skill_level=-1):
        key = "R"
        ability_value_dict = self.get_ability_values(key)[key][0]

        if skill_level > -1:
            self.bonus_attack_damage += self.total_attack_damage * (1 + (ability_value_dict["effect2"]["attribute0"][0][0][skill_level] / 100))
            self.set_base_stats_based_on_level()  # needs to be called everytime bonus AD changes

    def __getstate__(self):
        state = self.__dict__.copy()
        del state["champ_dict"]
        del state["stats"]
        del state["item_dict"]
        del state["has_passive"]
        return state

    def __setstate__(self, state):
        self.__dict__.update(state)
