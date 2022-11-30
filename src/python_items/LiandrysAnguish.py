from python_items.Item import Item
from Damage.Damage import Damage
from Damage.ScalingValue import ScalingValue
from Damage.DamageType import DamageType


class LiandrysAnguish(Item):

    def __init__(self, item_dict: dict):
        super().__init__(item_dict)
        self.is_mythic: bool = True
        self.is_uniqe: bool = True

    def item_passives_dmg(self, scaling_values: dict[str:ScalingValue] = {}, seconds_applied: int = 4, enemy_max_health: float = 0):
        damage = Damage(DamageType.MAGIC.value)
        damage_value: float = 0

        for key, value in scaling_values.items():
            if key == "AP":
                damage_value = (50 + (value.value * 0.06) +
                                (enemy_max_health * 0.04)) / 4

            damage.set_damage(damage_value * seconds_applied)
            return damage
