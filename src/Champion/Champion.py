from ..Ability.Bounds import Bounds

class Champion:

    def __init__(self, champ_dict):
        self.champ_dict = champ_dict
        # just for clarity so I don't have to write self.champ_dict["stats"] every time just self.stats
        self.stats = champ_dict["stats"]

        self.champion_id = self.champ_dict["id"]
        self.champion_name = self.champ_dict["name"]
        self.champion_icon = "https://" + self.champ_dict["icon"][7:]
        self.champion_resource = self.champ_dict["resource"]
        self.champion_attack_type = self.champ_dict["attackType"]
        self.champion_adaptive_type = self.champ_dict["adaptiveType"]

        self.champion_level = 1  # level 1 is standard can be changed with set_champion_level

        self.base_health = self.stats["health"]["flat"] * 1.0
        self.base_health_regen = self.stats["healthRegen"]["flat"] * 1.0
        self.base_mana = self.stats["mana"]["flat"] * 1.0
        self.base_mana_regen = self.stats["manaRegen"]["flat"] * 1.0
        self.base_armor = self.stats["armor"]["flat"] * 1.0
        self.base_magic_resistance = self.stats["magicResistance"]["flat"] * 1.0
        self.base_attack_damage = self.stats["attackDamage"]["flat"] * 1.0
        # This is a percentage
        self.base_attack_speed = self.stats["attackSpeed"]["flat"] * 1.0
        self.base_movespeed = self.stats["movespeed"]["flat"] * 1.0

        self.health_per_level = self.stats["health"]["perLevel"] * 1.0
        self.health_regen_per_level = self.stats["healthRegen"]["perLevel"] * 1.0
        self.mana_per_level = self.stats["mana"]["perLevel"] * 1.0
        self.mana_regen_per_level = self.stats["manaRegen"]["perLevel"] * 1.0
        self.armor_per_level = self.stats["armor"]["perLevel"] * 1.0
        self.magic_resistance_per_level = self.stats["magicResistance"]["perLevel"] * 1.0
        self.attack_damage_per_level = self.stats["attackDamage"]["perLevel"] * 1.0
        self.attack_speed_per_level = self.stats["attackSpeed"]["perLevel"] * 1.0

        # self.champ_dict["stats"]["criticalStrikeDamage"]["flat"] not correct in the jsons
        self.critical_strike_damage = 175.0
        self.critical_strike_damage_modifier = self.stats["criticalStrikeDamageModifier"]["flat"] * 1.0
        self.attack_speed_ratio = self.stats["attackSpeedRatio"]["flat"] * 1.0
        self.gold_per_10 = 20.4

        self.health_points_based_on_level = 0.0
        self.health_points_regen_based_on_level = 0.0
        self.mana_based_on_level = 0.0
        self.mana_regen_based_on_level = 0.0
        self.armor_based_on_level = 0.0
        self.magic_resistance_based_on_level = 0.0
        self.attack_damage_based_on_level = 0.0

        self.bonus_health_points = 0.0
        self.bonus_mana = 0.0
        self.bonus_armor = 0.0
        self.bonus_magic_resistance = 0.0
        self.bonus_attack_damage = 0.0
        self.bonus_attack_speed = 0.0

        self.total_health_points = 0.0
        self.total_health_regen = 0.0
        self.total_mana = 0.0
        self.total_mana_regen = 0.0
        self.total_armor = 0.0
        self.total_attack_damage = 0.0
        self.total_attack_speed = 0.0
        self.total_magic_resistance = 0.0
        self.total_armor_pen_percentage = 0.0
        self.total_magic_pen_percentage = 0.0
        self.total_tenacity = 0.0
        self.total_slow_resistance = 0.0

        self.total_critical_chance = 0.0
        self.total_lethality_flat = 0.0
        self.total_magic_pen_flat = 0.0
        self.total_ability_power_flat = 0.0
        self.total_ability_haste = 0.0
        self.total_heal_and_shield_power = 0.0
        self.total_life_steal = 0.0
        self.total_physical_vamp = 0.0
        self.total_omnivamp = 0.0

        self.item_dict = {
            "item1": None,
            "item2": None,
            "item3": None,
            "item4": None,
            "item5": None,
            "item6": None
        }
        self.has_mythic = False
        self.number_of_legendary_items = 0.0
        self.has_steraks_gage = False
        self.has_rabadons_deathcap = False
        self.has_titanic_hydra = False
        self.has_demonic_embrace = False

        self.mythic_armor_pen_perc = 0.0
        self.mythic_magic_pen_perc = 0.0
        self.mythic_tenacity = 0.0
        self.mythic_slow_resistance = 0.0

        self.q_bounds = Bounds(0, 5)
        self.w_bounds = Bounds(0, 5)
        self.e_bounds = Bounds(0, 5)
        self.r_bounds = Bounds(0, 3)

        self.q_name = self.champ_dict["abilities"]["Q"][0]["name"]
        self.w_name = self.champ_dict["abilities"]["W"][0]["name"]
        self.e_name = self.champ_dict["abilities"]["E"][0]["name"]
        self.r_name = self.champ_dict["abilities"]["R"][0]["name"]

        self.enemy_health = 0.0

    def set_champion_level(self, current_level):
        self.champion_level = current_level
        self.set_base_stats_based_on_level()

    def set_items_for_champion(self, item_dict):
        self.item_dict = item_dict

    def set_enemy_health(self, enemy_health):
        self.enemy_health = enemy_health

    def per_level_scaling(self, base_stat, growth_stat, round_by):
        return round(base_stat + growth_stat * (self.champion_level - 1) * (0.7025 + 0.0175 * (self.champion_level - 1)), round_by)

    def set_base_stats_based_on_level(self):
        self.health_points_based_on_level = self.per_level_scaling(
            self.base_health,
            self.health_per_level, 2)
        self.health_points_regen_based_on_level = self.per_level_scaling(
            self.base_health_regen,
            self.health_regen_per_level, 2)
        self.mana_based_on_level = self.per_level_scaling(
            self.base_mana,
            self.mana_per_level, 2)
        self.mana_regen_based_on_level = self.per_level_scaling(
            self.base_mana_regen,
            self.mana_regen_per_level, 2)
        self.armor_based_on_level = self.per_level_scaling(
            self.base_armor,
            self.armor_per_level, 2)
        self.magic_resistance_based_on_level = self.per_level_scaling(
            self.base_magic_resistance,
            self.magic_resistance_per_level, 2)
        self.attack_damage_based_on_level = self.per_level_scaling(
            self.base_attack_damage,
            self.attack_damage_per_level, 2)
        self.bonus_attack_speed = self.per_level_scaling(
            0,
            self.attack_speed_per_level / 100, 4)

    def set_total_value_to_based_on_level_and_item_stats(self):
        # First we add all the stats from the items that are chosen
        self.add_item_stats()
        self.add_mythic_stats()
        self.add_special_item_stats()

        #  Then we calculate the total damage based on the base stats and the bonus stats
        self.set_base_stats_based_on_level
        self.set_total_stats()

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

    def add_item_stats(self):
        for i in range(1, 7):
            curr_item = self.item_dict[f"item{i}"]
            if curr_item != None:

                if curr_item.is_legendary:
                    self.number_of_legendary_items += 1
                if curr_item.is_mythic:
                    self.has_mythic = True
                if curr_item.item_id == 3053:
                    self.has_steraks_gage = True
                if curr_item.item_id == 3089:
                    self.has_rabadons_deathcap == True
                if curr_item.item_id == 3748:
                    self.has_titanic_hydra = True
                if curr_item.item_id == 4637:
                    self.has_demonic_embrace = True

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

    def add_mythic_stats(self):
        if self.has_mythic:
            for i in range(int(self.number_of_legendary_items)):
                curr_item = self.item_dict[f"item{i}"]

                self.bonus_health_points += curr_item.mythic_health_flat
                self.bonus_armor += curr_item.mythic_armor_flat
                self.bonus_magic_resistance += curr_item.mythic_magic_resistance_flat
                self.bonus_attack_damage += curr_item.mythic_attack_damage_flat
                self.bonus_attack_speed += curr_item.mythic_attack_speed_flat

                self.total_lethality_flat += curr_item.mythic_lethality_flat
                self.total_magic_pen_flat += curr_item.mythic_magic_penetration_flat
                self.total_ability_power_flat += curr_item.mythic_ability_power_flat
                self.total_ability_haste += curr_item.mythic_ability_haste_flat
                self.total_heal_and_shield_power += curr_item.mythic_heal_and_shield_power_flat
                self.total_omnivamp += curr_item.mythic_omnivamp_flat_percentage

                self.mythic_armor_pen_perc += curr_item.mythic_armor_penetration_percentage
                self.mythic_magic_pen_perc += curr_item.mythic_magic_penetration_percentage
                self.mythic_tenacity += curr_item.mythic_tenacity_flat
                self.mythic_slow_resistance += curr_item.mythic_slow_resistance

        self.total_armor_pen_percentage = multiplicative_calc(
            self.total_armor_pen_percentage,
            self.mythic_armor_pen_perc
        )
        self.total_magic_pen_percentage = multiplicative_calc(
            self.total_magic_pen_percentage,
            self.mythic_magic_pen_perc
        )
        self.total_tenacity = multiplicative_calc(
            self.total_tenacity,
            self.mythic_tenacity
        )
        self.total_slow_resistance = multiplicative_calc(
            self.total_slow_resistance,
            self.mythic_slow_resistance
        )

    def add_special_item_stats(self):
        if self.has_steraks_gage:
            self.bonus_attack_damage += round(0.45 *
                                              self.attack_damage_based_on_level, 4)
        if self.has_rabadons_deathcap:
            self.total_ability_power_flat *= 1.35
        if self.has_titanic_hydra:
            self.bonus_attack_damage += round(0.02 *
                                              self.bonus_health_points, 4)
        if self.has_demonic_embrace:
            self.total_ability_power_flat += round(
                0.02 * self.bonus_health_points, 4)

    def set_total_stats(self):
        self.total_health_points = self.health_points_based_on_level + self.bonus_health_points
        self.total_mana = self.mana_based_on_level + self.bonus_mana
        self.total_armor = self.armor_based_on_level + self.bonus_armor
        self.total_magic_resistance = self.magic_resistance_based_on_level + \
            self.bonus_magic_resistance
        self.total_attack_damage = self.attack_damage_based_on_level + self.bonus_attack_damage

        self.total_attack_speed = round(
            self.base_attack_speed + (self.attack_speed_ratio * self.bonus_attack_speed), 2)

        self.total_armor_pen_percentage = round(
            1 - self.total_armor_pen_percentage, 4)
        self.total_magic_pen_percentage = round(
            1 - self.total_magic_pen_percentage, 4)
        self.total_tenacity = round(1 - self.total_tenacity, 4)
        self.total_slow_resistance = round(1 - self.total_slow_resistance, 4)

        self.total_critical_chance = round(self.total_critical_chance, 4)

    def __getstate__(self):
        state = self.__dict__.copy()
        del state["champ_dict"]
        del state["stats"]
        del state["item_dict"]
        return state

    def __setstate__(self, state):
        self.__dict__.update(state)


def multiplicative_calc(current_value, item_value):
    if current_value == 0:
        return round(1 - (item_value / 100), 4)
    else:
        return round(1 - (current_value * (item_value / 100)), 4)





