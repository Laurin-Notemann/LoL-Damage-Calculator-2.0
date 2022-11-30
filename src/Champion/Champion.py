from ChampionAbility.Bounds import Bounds
from ChampionAbility.Ability import Ability
from Damage.Damage import ScalingValue
from Utilities.AbilityUtils.get_abilities_data import get_abilities_data
from Damage.Damage import Damage


class Champion:

    def __init__(self, champ_dict):
        self.champ_dict: dict = champ_dict
        # just for clarity so I don't have to write self.champ_dict["stats"] every time just self.stats
        self.stats: dict = champ_dict["stats"]

        self.champion_id: int = self.champ_dict["id"]
        self.champion_name: str = self.champ_dict["name"]
        self.champion_icon: str = "https://" + self.champ_dict["icon"][7:]
        self.champion_resource: str = self.champ_dict["resource"]
        self.champion_attack_type: str = self.champ_dict["attackType"]
        self.champion_adaptive_type: str = self.champ_dict["adaptiveType"]

        # level 1 is standard can be changed with set_champion_level
        self.champion_level: int = 1

        self.base_health: float = self.stats["health"]["flat"]
        self.base_health_regen: float = self.stats["healthRegen"]["flat"]
        self.base_mana: float = self.stats["mana"]["flat"]
        self.base_mana_regen: float = self.stats["manaRegen"]["flat"]
        self.base_armor: float = self.stats["armor"]["flat"]
        self.base_magic_resistance: float = self.stats["magicResistance"]["flat"]
        self.base_attack_damage: float = self.stats["attackDamage"]["flat"]
        # This is a percentage
        self.base_attack_speed: float = self.stats["attackSpeed"]["flat"]
        self.base_movespeed: float = self.stats["movespeed"]["flat"]

        self.health_per_level: float = self.stats["health"]["perLevel"]
        self.health_regen_per_level: float = self.stats["healthRegen"]["perLevel"]
        self.mana_per_level: float = self.stats["mana"]["perLevel"]
        self.mana_regen_per_level: float = self.stats["manaRegen"]["perLevel"]
        self.armor_per_level: float = self.stats["armor"]["perLevel"]
        self.magic_resistance_per_level: float = self.stats["magicResistance"]["perLevel"]
        self.attack_damage_per_level: float = self.stats["attackDamage"]["perLevel"]
        self.attack_speed_per_level: float = self.stats["attackSpeed"]["perLevel"]

        # self.champ_dict["stats"]["criticalStrikeDamage"]["flat"] not correct in the jsons
        self.critical_strike_damage: float = 175.0
        self.critical_strike_damage_modifier: float = self.stats[
            "criticalStrikeDamageModifier"]["flat"]
        self.attack_speed_ratio: float = self.stats["attackSpeedRatio"]["flat"]
        self.gold_per_10: float = 20.4

        self.health_points_based_on_level: float = 0.0
        self.health_points_regen_based_on_level: float = 0.0
        self.mana_based_on_level: float = 0.0
        self.mana_regen_based_on_level = 0.0
        self.armor_based_on_level: float = 0.0
        self.magic_resistance_based_on_level: float = 0.0
        self.attack_damage_based_on_level: float = 0.0

        self.bonus_health_points: float = 0.0
        self.bonus_mana: float = 0.0
        self.bonus_armor: float = 0.0
        self.bonus_magic_resistance: float = 0.0
        self.bonus_attack_damage: float = 0.0
        self.bonus_attack_speed: float = 0.0

        self.total_health_points: float = 0.0
        self.total_health_regen: float = 0.0
        self.total_mana: float = 0.0
        self.total_mana_regen: float = 0.0
        self.total_armor: float = 0.0
        self.total_attack_damage: float = 0.0
        self.total_attack_speed: float = 0.0
        self.total_magic_resistance: float = 0.0
        self.total_armor_pen_percentage: float = 0.0
        self.total_magic_pen_percentage: float = 0.0
        self.total_tenacity: float = 0.0
        self.total_slow_resistance: float = 0.0

        self.total_critical_chance: float = 0.0
        self.total_lethality_flat: float = 0.0
        self.total_magic_pen_flat: float = 0.0
        self.total_ability_power_flat: float = 0.0
        self.total_ability_haste: float = 0.0
        self.total_heal_and_shield_power: float = 0.0
        self.total_life_steal: float = 0.0
        self.total_physical_vamp: float = 0.0
        self.total_omnivamp: float = 0.0

        self.item_dict: dict = {
            "item1": None,
            "item2": None,
            "item3": None,
            "item4": None,
            "item5": None,
            "item6": None
        }
        self.has_mythic: bool = False
        self.number_of_legendary_items: float = 0.0
        self.has_steraks_gage: bool = False
        self.has_rabadons_deathcap: bool = False
        self.has_titanic_hydra: bool = False
        self.has_demonic_embrace: bool = False

        self.mythic_armor_pen_perc: float = 0.0
        self.mythic_magic_pen_perc: float = 0.0
        self.mythic_tenacity: float = 0.0
        self.mythic_slow_resistance: float = 0.0

        # Bounds goes from 0 to 4 because values from json index start with 0
        self.q_bounds: Bounds = Bounds(0, 4)
        self.w_bounds: Bounds = Bounds(0, 4)
        self.e_bounds: Bounds = Bounds(0, 4)
        self.r_bounds: Bounds = Bounds(0, 4)

        # Data for a damage amplification based on missing health, only needed by a couple of champions
        self.missing_health_damage_amplifier = 0.0
        self.per_missing_health_percentage = 0.0
        self.missing_health_cap = 0.0

        self.q_name: str = self.champ_dict["abilities"]["Q"][0]["name"]
        self.w_name: str = self.champ_dict["abilities"]["W"][0]["name"]
        self.e_name: str = self.champ_dict["abilities"]["E"][0]["name"]
        self.r_name: str = self.champ_dict["abilities"]["R"][0]["name"]

        self.scaling_stats_values = {
            "AD": ScalingValue("AD", self.total_attack_damage),
            "bonus AD": ScalingValue("bonus AD", self.bonus_attack_damage),
            "AP": ScalingValue("AP", self.total_ability_power_flat)
        }

        # A list of abilities that contains the static information about the ability
        self.ability_q: list[Ability] = get_abilities_data(
            "Q", champ_dict, self.q_bounds)
        self.ability_w: list[Ability] = get_abilities_data(
            "W", champ_dict, self.w_bounds)
        self.ability_e: list[Ability] = get_abilities_data(
            "E", champ_dict, self.e_bounds)
        self.ability_r: list[Ability] = get_abilities_data(
            "R", champ_dict, self.r_bounds)

        self.add_scaling_stats_values_to_ability()

        self.enemy_health = 0.0

    def add_scaling_stats_values_to_ability(self):
        for i in range(len(self.ability_q)):
            self.ability_q[i].set_scaling_values(self.scaling_stats_values)
        for i in range(len(self.ability_w)):
            self.ability_w[i].set_scaling_values(self.scaling_stats_values)
        for i in range(len(self.ability_e)):
            self.ability_e[i].set_scaling_values(self.scaling_stats_values)
        for i in range(len(self.ability_r)):
            self.ability_r[i].set_scaling_values(self.scaling_stats_values)

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

    def set_scaling_values(self):
        self.scaling_stats_values = {
            "AD": ScalingValue("AD", self.total_attack_damage),
            "BONUS_AD": ScalingValue("BONUS_AD", self.bonus_attack_damage),
            "AP": ScalingValue("AP", self.total_ability_power_flat)
        }

    def set_total_value_to_based_on_level_and_item_stats(self):
        # First we add all the stats from the items that are chosen
        self.add_item_stats()
        self.add_mythic_stats()
        self.add_special_item_stats()

        #  Then we calculate the total damage based on the base stats and the bonus stats
        self.set_base_stats_based_on_level()
        self.set_total_stats()
        self.set_scaling_values()
        self.add_scaling_stats_values_to_ability()

    def auto_attack(self):
        damage_type = "PHYSICAL_DAMAGE"
        damage: Damage = Damage(damage_type)
        damage.set_damage(self.total_attack_damage)
        return damage

    def passive_action(self):
        pass

    def q_action(self, skill_level=-1):
        pass

    def w_action(self, skill_level=-1):
        pass

    def e_action(self, skill_level=-1):
        pass

    def r_action(self, skill_level=-1):
        pass

    def skill_level_inside_bounds(self, skill_level: int, ability: Ability):
        if ability.bounds.lower <= skill_level < ability.bounds.upper:
            return True
        return False

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
