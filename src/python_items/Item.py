from Damage.ScalingValue import ScalingValue
class Item:
    def __init__(self, item_dict):
        self.item_dict: dict = item_dict
        self.stats: dict = item_dict["stats"]  # for clarity

        self.item_id: int = self.item_dict["id"]
        self.item_name: str = self.item_dict["name"]
        self.item_icon: str = self.item_dict["icon"]

        self.item_tier: int = self.item_dict["tier"]
        # default False, will be changed to True inside the respctive item if it is a legendary item
        self.is_legendary: bool = False
        # default False, will be changed to True inside the respctive item if it is a mythic item
        self.is_mythic: bool = False

        self.item_builds_from: list[int] = self.item_dict["buildsFrom"]
        self.item_builds_into: list[int] = self.item_dict["buildsInto"]

        self.item_no_effects: bool = self.item_dict["noEffects"]
        self.item_passives: list[dict] = self.item_dict["passives"]
        self.item_actives: list[dict] = self.item_dict["active"]

        self.item_shop_price_total: int = self.item_dict["shop"]["prices"]["total"]
        self.item_shop_price_combined: int = self.item_dict["shop"]["prices"]["combined"]
        self.item_shop_price_sell: int = self.item_dict["shop"]["prices"]["sell"]

        # Just regular stats:
        self.item_ability_power_flat: float = self.stats["abilityPower"]["flat"]
        self.item_armor_flat: float = self.stats["armor"]["flat"]
        self.item_armor_penetration_percentage: float = self.stats["armorPenetration"]["percent"]
        self.item_attack_damage_flat: float = self.stats["attackDamage"]["flat"]
        self.item_attack_speed_flat: float = self.stats["attackSpeed"]["flat"]
        self.item_critical_strike_chance_percentage: float = self.stats[
            "criticalStrikeChance"]["percent"]
        self.item_gold_per_10_flat: float = self.stats["goldPer_10"]["flat"]
        self.item_heal_and_shield_power_flat: float = self.stats["healAndShieldPower"]["percent"]
        self.item_health_flat: float = self.stats["health"]["flat"]
        self.item_health_regen_flat: float = self.stats["healthRegen"]["flat"]
        self.item_lethality_flat: float = self.stats["lethality"]["flat"]
        self.item_lifesteal_percentage: float = self.stats["lifesteal"]["percent"]
        self.item_magic_penetration_flat: float = self.stats["magicPenetration"]["flat"]
        self.item_magic_penetration_percentage: float = self.stats["magicPenetration"]["percent"]
        self.item_magic_resistance_flat: float = self.stats["magicResistance"]["flat"]
        self.item_mana_flat: float = self.stats["mana"]["flat"]
        self.item_mana_regen_flat: float = self.stats["manaRegen"]["flat"]
        self.item_movespeed_flat: float = self.stats["movespeed"]["flat"]
        self.item_ability_haste_flat: float = self.stats["abilityHaste"]["flat"]
        self.item_omnivamp_percentage: float = self.stats["omnivamp"]["percent"]
        self.item_tenacity_flat: float = self.stats["omnivamp"]["flat"]
        self.item_slow_resistance_flat: float = 0
        self.item_physical_vamp: float = 0

        self.mythic_armor_flat: float = 0
        self.mythic_armor_penetration_percentage: float = 0
        self.mythic_ability_power_flat: float = 0
        self.mythic_attack_damage_flat: float = 0
        self.mythic_attack_speed_flat: float = 0
        self.mythic_heal_and_shield_power_flat: float = 0
        self.mythic_health_flat: float = 0
        self.mythic_lethality_flat: float = 0
        self.mythic_magic_penetration_flat: float = 0
        self.mythic_magic_penetration_percentage: float = 0
        self.mythic_magic_resistance_flat: float = 0
        # Movespeed for now irrelevant just a difficult calc for no reason lol
        # self.mythic_movespeed_flat = 0
        # self.mythic_movespeed_perc = 0
        self.mythic_ability_haste_flat: float = 0
        self.mythic_omnivamp_flat_percentage: float = 0
        self.mythic_tenacity_flat: float = 0
        # this has to be defined in the corresponing item (sunfire aegis)
        self.mythic_slow_resistance: float = 0

        self.has_active: bool = False
        self.is_unique: bool = False

        # Mythic item stats

    def set_mythic_stats(self):
        if self.item_no_effects == False and not self.item_passives:
            for item in self.item_passives:
                if item["mythic"]:
                    stats = item["stats"]  # for clarity
                    self.mythic_armor_flat = stats["armor"]["flat"]
                    self.mythic_armor_penetration_percentage = stats["armorPenetration"]["percent"]
                    self.mythic_ability_power_flat = stats["abilityPower"]["flat"]
                    self.mythic_attack_damage_flat = stats["attackDamage"]["flat"]
                    self.mythic_attack_speed_flat = stats["attackSpeed"]["flat"]
                    self.mythic_heal_and_shield_power_flat = stats["goldPer_10"]["percent"]
                    self.mythic_health_flat = stats["health"]["flat"]
                    self.mythic_lethality_flat = stats["lethality"]["flat"]
                    self.mythic_magic_penetration_flat = stats["magicPenetration"]["flat"]
                    self.mythic_magic_penetration_percentage = stats["magicPenetration"]["percent"]
                    self.mythic_magic_resistance_flat = stats["magicResistance"]["flat"]
                    # self.mythic_movespeed_flat = stats["movespeed"]["flat"]
                    # self.mythic_movespeed_perc = stats["movespeed"]["percent"]
                    self.mythic_ability_haste_flat = stats["abilityHaste"]["flat"]
                    self.mythic_omnivamp_flat_percentage = stats["omnivamp"]["percent"]
                    self.mythic_tenacity_flat = stats["omnivamp"]["flat"]

    def item_active_dmg(self):
        pass

    def item_passives_dmg(self, scaling_values: dict[str:ScalingValue] = {}):
        pass

    def __getstate__(self):
        state = self.__dict__.copy()
        del state["item_dict"]
        del state["stats"]
        del state["item_builds_from"]
        del state["item_builds_into"]
        del state["item_passives"]
        del state["item_actives"]
        return state

    def __setstate__(self, state):
        self.__dict__.update(state)
