from Utilities.DamageUtils.missingHealth import get_enemy_missing_health, get_amp_based_on_missing_health


class MissingHealthData:
    def __init__(self, enemy_total_health: float, enemy_current_hp: float, damage_amplifier: float, per_percentage_of_missing_health: float, missing_health_cap: float):
        self.enemy_total_health: float = enemy_total_health
        self.enemy_missing_health: float = get_enemy_missing_health(
            enemy_total_health, enemy_current_hp)
        # divided by 1000 for a more precise calculation
        self.damage_amplifier: float = damage_amplifier/2500
        self.per_percentage_of_missing_health: float = per_percentage_of_missing_health/2500
        # a percentage that amplifies the damage dealt
        self.missing_health_cap: float = missing_health_cap
        self.amplifier: float = get_amp_based_on_missing_health(
            self.enemy_missing_health,
            self.damage_amplifier,
            self.per_percentage_of_missing_health,
            self.missing_health_cap
        )

    def update_missing_health(self, enemy_current_hp: float):
        self.enemy_missing_health = get_enemy_missing_health(
            self.enemy_total_health, enemy_current_hp)
        self.amplifier = get_amp_based_on_missing_health(
            self.enemy_missing_health,
            self.damage_amplifier,
            self.per_percentage_of_missing_health,
            self.missing_health_cap
        )
