class Damage:

    # secondary damage only relevant if type = "MIXED_DAMAGE"
    def __init__(self, type: str, primary_damage: float, secondary_damage: float):
        self.type = type
        self.primary_damage = primary_damage
        self.secondary_damage = secondary_damage
