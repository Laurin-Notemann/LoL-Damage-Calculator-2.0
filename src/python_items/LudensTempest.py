from python_items.Item import Item
from Damage.Damage import Damage
from Damage.DamageType import DamageType
from Damage.ScalingValue import ScalingValue

class LudensTempest(Item):

    def __init__(self, item_dict: dict):
        super().__init__(item_dict)
        self.is_mythic: bool = True
        self.is_uniqe: bool = True

    def item_passives_dmg(self, scaling_values: dict[str:ScalingValue] = {}):
        damage = Damage(DamageType.MAGIC.value)
        damage_value: float = 0
        for key, value in scaling_values:
            if key == "AP":
                damage_value = 100 + (value.value * 0.1)
                damage.set_damage(damage_value)
                return damage

