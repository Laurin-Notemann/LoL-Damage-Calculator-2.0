from python_items.Item import Item


class LiandrysAnguish(Item):

    def __init__(self, item_dict: dict):
        super().__init__(item_dict)
        self.is_mythic: bool = True
        self.is_uniqe: bool = True

    def item_passives_dmg(self, champions_scaling_param: str = "", champion_scaling_value: float = 0, seconds_applied: int = 4, enemy_max_health: float = 0):
        damage_type: str = "MAGIC_DAMAGE"
        damage: float = 0

        if champions_scaling_param == "AP":
            damage = (50 + (champion_scaling_value * 0.06) +
                      (enemy_max_health * 0.04)) / 4

            damage = damage * seconds_applied

        return [damage_type, damage, None]
