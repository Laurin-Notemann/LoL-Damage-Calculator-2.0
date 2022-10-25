
class Champion:

    def __init__(self, champ_dict):
        self.champ_dict = champ_dict

        self.champion_id = self.champ_dict["id"]
        self.champion_name = self.champ_dict["name"]

        self.champion_resource = self.champ_dict["resource"]
        self.champion_attack_type = self.champ_dict["attackType"]
        self.champion_adaptive_type = self.champ_dict["adaptiveType"]

        self.champion_level = 1

        self.base_health = self.champ_dict["stats"]["health"]["flat"]
        self.health_per_level = self.champ_dict["stats"]["health"]["perLevel"]
        self.base_health_regen = self.champ_dict["stats"]["healthRegen"]["flat"]
        self.health_regen_per_level = self.champ_dict["stats"]["healthRegen"]["perLevel"]

        self.base_mana = self.champ_dict["stats"]["mana"]["flat"]
        self.mana_per_level = self.champ_dict["stats"]["mana"]["perLevel"]

        self.base_mana_regen = self.champ_dict["stats"]["manaRegen"]["flat"]
        self.mana_regen_per_level = self.champ_dict["stats"]["manaRegen"]["perLevel"]

        self.base_armor = self.champ_dict["stats"]["armor"]["flat"]
        self.armor_per_level = self.champ_dict["stats"]["armor"]["perLevel"]

        self.base_magic_resistance = self.champ_dict["stats"]["magicResistance"]["flat"]
        self.magic_resistance_per_level = self.champ_dict["stats"]["magicResistance"]["perLevel"]

        self.base_attack_damage = self.champ_dict["stats"]["attackDamage"]["flat"]
        self.attack_damage_flat_per_level = self.champ_dict["stats"]["attackDamage"]["perLevel"]

        self.base_movespeed = self.champ_dict["stats"]["movespeed"]["flat"]

        self.critical_strike_damage = 175  # self.champ_dict["stats"]["criticalStrikeDamage"]["flat"]
        self.critical_strike_damage_modifier = self.champ_dict["stats"]["criticalStrikeDamageModifier"]["flat"]

        self.base_attack_speed = self.champ_dict["stats"]["attackSpeed"]["flat"]
        self.attack_speed_per_level = self.champ_dict["stats"]["attackSpeed"]["perLevel"]  # This is a percentage
        self.attack_speed_ratio = self.champ_dict["stats"]["attackSpeedRatio"]["flat"]

        self.ability_power_flat = None

        self.armor_pen_percentage = None
        self.lethality_flat = None

        self.ability_haste = None

        self.magic_pen_percentage = None
        self.magic_pen_flat = None

        self.life_steal = None
        self.physical_vamp = None
        self.omnivamp = None

        self.gold_per_10 = None

        self.heal_and_shield_power = None
        self.tenacity = None
        self.slow_resistance = None

        self.health_points_based_on_level = None
        self.health_points_regen_based_on_level = None
        self.mana_based_on_level = None
        self.mana_regen_based_on_level = None
        self.armor_based_on_level = None
        self.magic_resistance_based_on_level = None
        self.attack_damage_based_on_level = None
        self.bonus_attack_speed = None

        self.bonus_armor_flat = None
        self.bonus_magic_resistance = None
        self.bonus_attack_damage = None
        self.bonus_health_points = None
        self.bonus_mana = None

        self.total_armor = None
        self.total_magic_resistance = None
        self.total_attack_damage = None
        self.total_health_points = None
        self.total_mana = None
        self.total_attack_speed = None

        self.passive_ability_dict = self.get_ability_values("P")["P"][0]
        # self.q_ability_dict = self.get_ability_values("Q")["Q"][0]
        # self.w_ability_dict = self.get_ability_values("W")["W"][0]
        # self.e_ability_dict = self.get_ability_values("E")["E"][0]
        # self.r_ability_dict = self.get_ability_values("R")["R"][0]

    def set_champion_level(self, current_level):
        self.champion_level = current_level

    def per_level_scaling(self, base_stat, growth_stat):
        return round(base_stat + growth_stat * (self.champion_level - 1) * (0.7025 + 0.0175 * (self.champion_level - 1)), 2)

    def set_base_stats_based_on_leve(self):
        self.health_points_based_on_level = self.per_level_scaling(self.base_health, self.health_per_level)
        self.health_points_regen_based_on_level = self.per_level_scaling(self.base_health_regen, self.health_regen_per_level)
        self.mana_based_on_level = self.per_level_scaling(self.base_mana, self.mana_per_level)
        self.mana_regen_based_on_level = self.per_level_scaling(self.base_mana_regen, self.mana_regen_per_level)
        self.

    def something(self, key, skill_level, effect_number, attribute_number, scaling_param):
        damage_total_without_amp = self.get_dmg_based_on_flat_and_percentage_values(key, skill_level, effect_number, attribute_number, scaling_param)
        return [damage_total_without_amp[1], round(damage_total_without_amp[0], 3)]

    def auto_attack(self):
        return ["PHYSICAL_DAMAGE", self.base_attack_damage]

    def passive_ability(self):
        pass

    def q_ability(self, skill_level=-1):
        pass

    def w_ability(self, skill_level=-1):
        pass

    def e_ability(self, skill_level=-1):
        pass

    def r_ability(self, skill_level=-1):
        pass

    def get_missing_hp_percentage(self, enemy_current_hp, enemy_max_hp):
        pass

    def get_dmg_based_on_flat_and_percentage_values(self, key, skill_level, effect_number, attribute_number, scaling_param: str):
        """

        :param scaling_param:
        :param attribute_number:
        :param effect_number:
        :param key:
        :param skill_level:
        :return:
        """
        scaling_value = None
        if scaling_param == "AD":
            scaling_value = self.base_attack_damage
        elif scaling_param == "AP":
            scaling_value = self.ability_power_flat
        if skill_level > -1:
            ability_value_dict = self.get_ability_values(key)[key][0]

            damage_type = ability_value_dict["damage_type"]
            damage_flat = ability_value_dict[f"effect{effect_number}"][f"attribute{attribute_number}"][0][0]
            damage_scaling = []
            for i in ability_value_dict[f"effect{effect_number}"][f"attribute{attribute_number}"][1][0]:
                damage_scaling.append((i / 100) * scaling_value)

            return [damage_flat[skill_level] + damage_scaling[skill_level], damage_type]

    def get_ability_values(self, key):
        ability_dict = self.champ_dict["abilities"][key]

        ability_attribute_modifier_value = {key: [{}]}

        for ability_number in range(len(ability_dict)):
            for effect_number in range(len(ability_dict[ability_number]["effects"])):
                ability_attribute_modifier_value[key][ability_number][f"effect{effect_number}"] = {}
                for attribute_number in range(len(ability_dict[ability_number]["effects"][effect_number]["leveling"])):
                    ability_attribute_modifier_value[key][ability_number][f"effect{effect_number}"][f"attribute{attribute_number}"] = []
                    for modifier_number in range(
                            len(ability_dict[ability_number]["effects"][effect_number]["leveling"][attribute_number]["modifiers"])):
                        effect_mod_values = \
                            ability_dict[ability_number]["effects"][effect_number]["leveling"][attribute_number]["modifiers"][modifier_number][
                                "values"]
                        effect_mod_unit = \
                            ability_dict[ability_number]["effects"][effect_number]["leveling"][attribute_number]["modifiers"][modifier_number][
                                "units"]
                        ability_attribute_modifier_value[key][ability_number][f"effect{effect_number}"][f"attribute{attribute_number}"].append(
                            [effect_mod_values, effect_mod_unit])

            if ability_dict[ability_number]["cost"] is not None:
                for modifier_umber in range(len(ability_dict[ability_number]["cost"]["modifiers"])):
                    cost_mod_value = ability_dict[ability_number]["cost"]["modifiers"][modifier_umber]["values"]
                    ability_attribute_modifier_value[key][ability_number]["cost"] = cost_mod_value

            if ability_dict[ability_number]["cooldown"] is not None:
                for modifier_umber in range(len(ability_dict[ability_number]["cooldown"]["modifiers"])):
                    cooldown_mod_value = ability_dict[ability_number]["cooldown"]["modifiers"][modifier_umber]["values"]
                    ability_attribute_modifier_value[key][ability_number]["cooldown"] = cooldown_mod_value

            ability_attribute_modifier_value[key][ability_number]["damage_type"] = ability_dict[ability_number]["damageType"]

        return ability_attribute_modifier_value
