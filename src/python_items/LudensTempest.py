from python_items.Item import Item


class LudensTempest(Item):

    def __init__(self, item_dict: dict):
        super().__init__(item_dict)
        self.is_mythic: bool = True
        self.is_uniqe: bool = True

    def item_passives_dmg(self, champions_scaling_param: str = "", champion_scaling_value: float = 0):
        damage_type: str = "MAGIC_DAMAGE"
        damage: float = 0
        if champions_scaling_param == "AP":
            damage = 100 + (champion_scaling_value * 0.1)

        return [damage_type, damage, None]
