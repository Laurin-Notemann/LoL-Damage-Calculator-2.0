from python_items.Item import Item


class LiandrysAnguish(Item):

    def __init__(self, item_dict):
        super().__init__(item_dict)
        self.is_mythic = True

    def item_passives_dmg(self, champions_scaling_param: str = "", champion_scaling_value=0, seconds_applied=4, enemy_max_health=0):
        damage_type = "MAGIC_DAMAGE"
        damage = 0

        if champions_scaling_param == "AP":
            damage = (50 + (champion_scaling_value * 0.06) +
                      (enemy_max_health * 0.04)) / 4

            damage = damage * seconds_applied

        return [damage_type, damage, None]
