from src.python_champions.get_dict import get_dict
from src.python_items.Item import Item


class LudensTempest(Item):

    def item_passives_dmg(self, champions_scaling_param: str = "", champion_scaling_value=0):
        damage_type = "MAGIC_DAMAGE"
        damage = 0
        if champions_scaling_param == "AP":
            damage = 100 + (champion_scaling_value * 0.1)

        return [damage_type, damage, None]


ludens = LudensTempest(get_dict("6655"))

print(ludens.item_passives_dmg("AP", 1000))
