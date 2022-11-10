import jsonpickle


class Champion:

    def __init__(self, champ_dict):
        self.champ_dict = champ_dict
        # just for clarity so I don't have to write self.champ_dict["stats"] every time just self.stats
        self.stats = champ_dict["stats"]

        self.champion_id = self.champ_dict["id"]
        self.champion_name = self.champ_dict["name"]
        self.champion_icon = self.champ_dict["icon"]

        self.champion_resource = self.champ_dict["resource"]
        self.champion_attack_type = self.champ_dict["attackType"]
        self.champion_adaptive_type = self.champ_dict["adaptiveType"]

        self.champion_level = 1 # level 1 is standard can be changed with set_champion_level

        self.base_health = self.stats["health"]["flat"]
        self.base_health_regen = self.stats["healthRegen"]["flat"]
        self.base_mana = self.stats["mana"]["flat"]
        self.base_mana_regen = self.stats["manaRegen"]["flat"]
        self.base_armor = self.stats["armor"]["flat"]
        self.base_magic_resistance = self.stats["magicResistance"]["flat"]
        self.base_attack_damage = self.stats["attackDamage"]["flat"]
        self.base_attack_speed = self.stats["attackSpeed"]["flat"] # This is a percentage
        self.base_movespeed = self.stats["movespeed"]["flat"]

        self.health_per_level = self.stats["health"]["perLevel"]
        self.health_regen_per_level = self.stats["healthRegen"]["perLevel"]
        self.mana_per_level = self.stats["mana"]["perLevel"]
        self.mana_regen_per_level = self.stats["manaRegen"]["perLevel"]
        self.armor_per_level = self.stats["armor"]["perLevel"]
        self.magic_resistance_per_level = self.stats["magicResistance"]["perLevel"]
        self.attack_damage_per_level = self.stats["attackDamage"]["perLevel"]
        self.attack_speed_per_level = self.stats["attackSpeed"]["perLevel"]

        # self.champ_dict["stats"]["criticalStrikeDamage"]["flat"] not correct in the jsons
        self.critical_strike_damage = 175
        self.critical_strike_damage_modifier = self.stats["criticalStrikeDamageModifier"]["flat"]
        self.attack_speed_ratio = self.stats["attackSpeedRatio"]["flat"]
        self.gold_per_10 = 20.4

        self.health_points_based_on_level = 0
        self.health_points_regen_based_on_level = 0
        self.mana_based_on_level = 0
        self.mana_regen_based_on_level = 0
        self.armor_based_on_level = 0
        self.magic_resistance_based_on_level = 0
        self.attack_damage_based_on_level = 0

        self.bonus_health_points = 0
        self.bonus_mana = 0
        self.bonus_armor = 0
        self.bonus_magic_resistance = 0
        self.bonus_attack_damage = 0
        self.bonus_attack_speed = 0 

        self.total_health_points = 0
        self.total_health_regen = 0
        self.total_mana = 0
        self.total_mana_regen = 0
        self.total_armor = 0
        self.total_magic_resistance = 0
        self.mythic_magic_pen_percentage = 0
        self.mythic_tenacity = 0
        self.mythic_slow_resistance = 0
        self.total_attack_damage = 0

        self.total_critical_chance = 0
        self.total_lethality_flat = 0
        self.total_magic_pen_flat = 0
        self.total_ability_power_flat = 0
        self.total_ability_haste = 0
        self.total_heal_and_shield_power = 0
        self.total_life_steal = 0
        self.total_physical_vamp = 0
        self.total_omnivamp = 0

        # following to method calls only for test purposes
        self.set_base_stats_based_on_level()
        # self.set_total_value_to_based_on_level_and_item_stats()

        self.passive_ability_dict = self.get_ability_values("P")["P"][0]
        # self.q_ability_dict = self.get_ability_values("Q")["Q"][0]
        # self.w_ability_dict = self.get_ability_values("W")["W"][0]
        # self.e_ability_dict = self.get_ability_values("E")["E"][0]
        # self.r_ability_dict = self.get_ability_values("R")["R"][0]

    def set_champion_level(self, current_level):
        self.champion_level = current_level

    def per_level_scaling(self, base_stat, growth_stat, round_by):
        return round(base_stat + growth_stat * (self.champion_level - 1) * (0.7025 + 0.0175 * (self.champion_level - 1)), round_by)

    def set_base_stats_based_on_level(self):
        self.health_points_based_on_level = self.per_level_scaling(
            self.base_health, self.health_per_level, 2)
        self.health_points_regen_based_on_level = self.per_level_scaling(
            self.base_health_regen, self.health_regen_per_level, 2)
        self.mana_based_on_level = self.per_level_scaling(
            self.base_mana, self.mana_per_level, 2)
        self.mana_regen_based_on_level = self.per_level_scaling(
            self.base_mana_regen, self.mana_regen_per_level, 2)
        self.armor_based_on_level = self.per_level_scaling(
            self.base_armor, self.armor_per_level, 2)
        self.magic_resistance_based_on_level = self.per_level_scaling(
            self.base_magic_resistance, self.magic_resistance_per_level, 2)
        self.attack_damage_based_on_level = self.per_level_scaling(
            self.base_attack_damage, self.attack_damage_per_level, 2)
        self.bonus_attack_speed = self.per_level_scaling(
            0, self.attack_speed_per_level / 100, 4)

    def set_total_value_to_based_on_level_and_item_stats(self, item_dict: dict):
        """
        only for test purposes, champion uses total attack damage for auto attacks, which depend on item, but items not yet done
        :return:
        """
        # First we set all the bonus stats

        for i in range(1, 7):
            if item_dict[f"item{i}"] != "":
                curr_item = item_dict[f"item{i}"]

                self.bonus_health_points += curr_item.item_health_flat
                self.bonus_mana += curr_item.item_mana_flat
                self.bonus_armor += curr_item.item_armor_flat
                self.bonus_magic_resistance += curr_item.item_magic_resistance_flat
                self.bonus_attack_damage += curr_item.item_attack_damage_flat
                self.bonus_attack_speed += curr_item.item_attack_speed_flat

                self.total_critical_chance += curr_item.item_critical_strike_chance_percentage
                self.total_lethality_flat += curr_item.item_lethality_flat
                self.total_magic_pen_flat += curr_item.item_magic_penetration_flat
                self.total_ability_power_flat += curr_item.item_ability_power_flat
                self.total_ability_haste += curr_item.item_ability_haste_flat
                self.total_heal_and_shield_power += curr_item.item_heal_and_shield_power_flat
                self.total_life_steal += curr_item.item_lifesteal_percentage
                self.total_physical_vamp += curr_item.item_physical_vamp
                self.total_omnivamp += curr_item.item_omnivamp_percentage

                self.total_armor_pen_percentage = multiplicative_calc(
                    self.total_armor_pen_percentage,
                    curr_item.item_armor_penetration_percentage
                )
                self.total_magic_pen_percentage = multiplicative_calc(
                    self.total_magic_pen_percentage,
                    curr_item.item_magic_penetration_percentage
                )
                self.total_tenacity = multiplicative_calc(
                    self.total_tenacity, 
                    curr_item.item_tenacity_flat
                )
                self.total_slow_resistance = multiplicative_calc(
                    self.total_slow_resistance, 
                    curr_item.item_slow_resistance_flat
                )

                if curr_item.item_health_regen_flat > 0:
                    self.total_health_regen += self.base_health_regen * \
                        curr_item.item_health_regen_flat
                if curr_item.item_mana_regen_flat > 0:
                    self.total_mana_regen += self.base_mana_regen * curr_item.item_mana_regen_flat

        #  Then we calculate the total damage based on the base stats and the bonus stats
        self.total_attack_damage = self.attack_damage_based_on_level + self.bonus_attack_damage
        self.total_health_points = self.health_points_based_on_level + self.bonus_health_points
        self.total_mana = self.mana_based_on_level + self.bonus_mana
        self.total_armor = self.armor_based_on_level + self.bonus_armor
        self.total_magic_resistance = self.magic_resistance_based_on_level + \
            self.bonus_magic_resistance

        self.total_armor_pen_percentage = round(
            1 - self.total_armor_pen_percentage, 4)
        self.total_magic_pen_percentage = round(
            1 - self.total_magic_pen_percentage, 4)
        self.total_tenacity = round(1 - self.total_tenacity, 4)
        self.total_slow_resistance = round(1 - self.total_slow_resistance, 4)

    def auto_attack(self):
        return ["PHYSICAL_DAMAGE", self.total_attack_damage, None]

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

    def get_missing_health(self, enemy_max_hp, enemy_current_hp):
        return round((enemy_max_hp - enemy_current_hp) / enemy_max_hp, 6)

    def get_amp_based_on_missing_health(self, enemy_missing_health_perc, missing_health_iterator_static, damage_amplifier_missing_health_static,
                                        missing_health_cap):
        missing_health_iterator = missing_health_iterator_static
        damage_amplifier_missing_health = damage_amplifier_missing_health_static
        for i in range(0, int((missing_health_cap / missing_health_iterator)) + 1):
            if enemy_missing_health_perc < missing_health_iterator_static:
                damage_amplifier_missing_health = 0
                break
            elif missing_health_iterator < enemy_missing_health_perc < (
                    missing_health_iterator + missing_health_iterator_static) or enemy_missing_health_perc == missing_health_iterator:
                break
            missing_health_iterator = round(
                missing_health_iterator + missing_health_iterator_static, 5)
            damage_amplifier_missing_health = round(
                damage_amplifier_missing_health + damage_amplifier_missing_health_static, 5)

        return damage_amplifier_missing_health

    def get_dmg_based_on_flat_and_percentage_values(self, key, skill_level, effect_number, attribute_number, scaling_param: str,
                                                    scaling_param_two: str = ""):
        """

        :param scaling_param_two:
        :param scaling_param:
        :param attribute_number:
        :param effect_number:
        :param key:
        :param skill_level:
        :return:
        """
        scaling_value_one = 0
        scaling_value_two = 0
        if scaling_param == "AD":
            scaling_value_one = self.total_attack_damage
        elif scaling_param == "BONUS_AD":
            scaling_value_one = self.bonus_attack_damage
        elif scaling_param == "AP":
            scaling_value_one = self.total_ability_power_flat

        if scaling_param_two:
            if scaling_param_two == "AD":
                scaling_value_two = self.total_attack_damage
            elif scaling_param_two == "BONUS_AD":
                scaling_value_two = self.bonus_attack_damage
            elif scaling_param_two == "AP":
                scaling_value_two = self.total_ability_power_flat

        if skill_level > -1:
            ability_value_dict = self.get_ability_values(key)[key][0]

            damage_type = ability_value_dict["damage_type"]
            damage_flat = ability_value_dict[f"effect{effect_number}"][f"attribute{attribute_number}"][0][0]
            damage_scaling_one = []
            damage_scaling_two = []
            for i in ability_value_dict[f"effect{effect_number}"][f"attribute{attribute_number}"][1][0]:
                damage_scaling_one.append((i / 100) * scaling_value_one)

            if scaling_param_two:
                for i in ability_value_dict[f"effect{effect_number}"][f"attribute{attribute_number}"][2][0]:
                    damage_scaling_two.append((i / 100) * scaling_value_two)
            if scaling_param_two:
                return [damage_flat[skill_level] + damage_scaling_one[skill_level] + damage_scaling_two[skill_level], damage_type]
            return [damage_flat[skill_level] + damage_scaling_one[skill_level], damage_type]

    def wrapper_for_dmg(self, key, skill_level, effect_number, attribute_number, scaling_param: str, scaling_param_two: str = ""):
        """
        This function is just a simple wrapper for clarity when reading the code, which also rounds the dmg number.
        Third Parameter in the return call is None because when to make the array that contains the damage numbers consistent, reason being if the
        dmg is mixed (e.g. Physical and Magical) then you get three parameters, first one states the type of dmg, and the other to each instance of
        the mixed dmg.
        :param scaling_param_two:
        :param key:
        :param skill_level:
        :param effect_number:
        :param attribute_number:
        :param scaling_param:
        :return:
        """
        damage_total_without_amp = self.get_dmg_based_on_flat_and_percentage_values(key, skill_level, effect_number, attribute_number,
                                                                                    scaling_param, scaling_param_two)
        return [damage_total_without_amp[1], round(damage_total_without_amp[0], 3), None]

    def get_ability_values(self, key):
        ability_dict = self.champ_dict["abilities"][key]

        ability_attribute_modifier_value = {key: [{}]}

        for ability_number in range(len(ability_dict)):
            for effect_number in range(len(ability_dict[ability_number]["effects"])):
                ability_attribute_modifier_value[key][ability_number][f"effect{effect_number}"] = {
                }
                for attribute_number in range(len(ability_dict[ability_number]["effects"][effect_number]["leveling"])):
                    ability_attribute_modifier_value[key][ability_number][f"effect{effect_number}"][f"attribute{attribute_number}"] = [
                    ]
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

            ability_attribute_modifier_value[key][ability_number][
                "damage_type"] = ability_dict[ability_number]["damageType"]

        return ability_attribute_modifier_value

    def set_champion_level(self, level):
        self.champion_level = level

    def __getstate__(self):
        state = self.__dict__.copy()
        del state["champ_dict"]
        return state

    def __setstate__(self, state):
        self.__dict__.update(state)


def multiplicative_calc(current_value, item_value):
    if current_value == 0:
        return round(1 - (item_value / 100), 4)
    else:
        return round(1 - (current_value * (item_value / 100)), 4)
