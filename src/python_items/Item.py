import json


class Item:
    def __init__(self, item_dict):
        self.item_dict = item_dict

        self.item_id = self.item_dict["id"]
        self.item_name = self.item_dict["name"]

        self.item_tier = self.item_dict["tier"]

        self.item_builds_from = self.item_dict["buildsFrom"]
        self.item_builds_into = self.item_dict["buildsInto"]

        self.item_no_effects = self.item_dict["noEffects"]
        self.item_passives = self.item_dict["passives"]
        self.item_actives = self.item_dict["active"]

        self.item_shop_price_total = self.item_dict["shop"]["prices"]["total"]
        self.item_shop_price_combined = self.item_dict["shop"]["prices"]["combined"]
        self.item_shop_price_sell = self.item_dict["shop"]["prices"]["sell"]

        # Just regular stats:
        self.item_ability_power_flat = self.item_dict["stats"]["abilityPower"]["flat"]
        self.item_armor_flat = self.item_dict["stats"]["armor"]["flat"]
        self.item_armor_penetration_percentage = self.item_dict["stats"]["armorPenetration"]["percent"]
        self.item_attack_damage_flat = self.item_dict["stats"]["attackDamage"]["flat"]
        self.item_attack_speed_flat = self.item_dict["stats"]["attackSpeed"]["flat"]
        self.item_critical_strike_chance_percentage = self.item_dict["stats"]["criticalStrikeChance"]["percent"]
        self.item_gold_per_10_flat = self.item_dict["stats"]["goldPer_10"]["flat"]
        self.item_heal_and_shield_power_flat = self.item_dict["stats"]["healAndShieldPower"]["percent"]
        self.item_health_flat = self.item_dict["stats"]["health"]["flat"]
        self.item_health_regen_flat = self.item_dict["stats"]["healthRegen"]["flat"]
        self.item_lethality_flat = self.item_dict["stats"]["lethality"]["flat"]
        self.item_lifesteal_percentage = self.item_dict["stats"]["lifesteal"]["percent"]
        self.item_magic_penetration_flat = self.item_dict["stats"]["magicPenetration"]["flat"]
        self.item_magic_penetration_percentage = self.item_dict["stats"]["magicPenetration"]["percent"]
        self.item_magic_resistance_flat = self.item_dict["stats"]["magicResistance"]["flat"]
        self.item_mana_flat = self.item_dict["stats"]["mana"]["flat"]
        self.item_mana_regen_flat = self.item_dict["stats"]["manaRegen"]["flat"]
        self.item_movespeed_flat = self.item_dict["stats"]["movespeed"]["flat"]
        self.item_ability_haste_flat = self.item_dict["stats"]["abilityHaste"]["flat"]
        self.item_omnivamp_percentage = self.item_dict["stats"]["omnivamp"]["percent"]
        self.item_tenacity_flat = self.item_dict["stats"]["omnivamp"]["flat"]
        self.item_slow_resistance_flat = 0
        self.item_physical_vamp = 0

        self.mythic_armor_flat = 0
        self.mythic_armor_penetration_percentage = 0
        self.mythic_ability_power_flat = 0
        self.mythic_attack_damage_flat = 0
        self.mythic_attack_speed_flat = 0
        self.mythic_heal_and_shield_power_flat = 0
        self.mythic_health_flat = 0
        self.mythic_lethality_flat = 0
        self.mythic_magic_penetration_flat = 0
        self.mythic_magic_penetration_percentage = 0
        self.mythic_magic_resistance_flat = 0
        self.mythic_movespeed_flat = 0
        self.mythic_movespeed_perc = 0
        self.mythic_ability_haste_flat = 0
        self.mythic_omnivamp_flat_percentage = 0
        self.mythic_tenacity_flat = 0

        # Mythic item stats
        if self.item_no_effects == False and not self.item_passives:
            for item in self.item_passives:
                if item["mythic"]:
                    self.mythic_armor_flat = item["stats"]["armor"]["flat"]
                    self.mythic_armor_penetration_percentage = item["stats"]["armorPenetration"]["percent"]
                    self.mythic_ability_power_flat = item["stats"]["abilityPower"]["flat"]
                    self.mythic_attack_damage_flat = item["stats"]["attackDamage"]["flat"]
                    self.mythic_attack_speed_flat = item["stats"]["attackSpeed"]["flat"]
                    self.mythic_heal_and_shield_power_flat = item["stats"]["goldPer_10"]["percent"]
                    self.mythic_health_flat = item["stats"]["health"]["flat"]
                    self.mythic_lethality_flat = item["stats"]["lethality"]["flat"]
                    self.mythic_magic_penetration_flat = item["stats"]["magicPenetration"]["flat"]
                    self.mythic_magic_penetration_percentage = item["stats"]["magicPenetration"]["percent"]
                    self.mythic_magic_resistance_flat = item["stats"]["magicResistance"]["flat"]
                    self.mythic_movespeed_flat = item["stats"]["movespeed"]["flat"]
                    self.mythic_movespeed_perc = item["stats"]["movespeed"]["percent"]
                    self.mythic_ability_haste_flat = item["stats"]["abilityHaste"]["flat"]
                    self.mythic_omnivamp_flat_percentage = item["stats"]["omnivamp"]["percent"]
                    self.mythic_tenacity_flat = item["stats"]["omnivamp"]["flat"]

    def item_active_dmg(self):
        pass

    def item_passives_dmg(self, champions_scaling_param: str = "", champion_scaling_value=0):
        pass

    def get_stats_from_json(self):
        pass
