from src.python_champions.get_dict import get_dict
from src.python_items.Item import Item


class LiandrysAnguish(Item):
    def item_passives_dmg(self, champions_scaling_param: str = "", champion_scaling_value=0, seconds_applied=4, enemy_max_health=0):
        damage_type = "MAGIC_DAMAGE"
        damage = 0

        if champions_scaling_param == "AP":
            damage = (50 + (champion_scaling_value * 0.06) + (enemy_max_health * 0.04)) / 4

            damage = damage * seconds_applied

        return [damage_type, damage, None]


liandrys = LiandrysAnguish(get_dict("6653"))

print(liandrys.item_passives_dmg("AP", 1000, 4, 5000))
