from python_champions.Seraphine.Seraphine import Seraphine
from python_champions.Ahri.Ahri import Ahri
from python_items.LudensTempest.LudensTempest import LudensTempest
from python_champions.get_dict import get_dict_champ, get_dict_item

import jsonpickle
"""
ability_dict = {
    "Q": [
        {
            "effects1": {
                "attribute1": [
                    ["values", "unit"], ["values", "unit"], ["values", "unit"]
                ],
                "attribute2": [
                    ["values", "unit"]
                ],
                "attribute3": [
                    ["values", "unit"], ["values", "unit"]
                ]
            },
            "effects2": {
                "attribute1": [
                    ["values", "unit"], ["values", "unit"]
                ],
                "attribute2": [
                    ["values", "unit"], ["values", "unit"]
                ]
            },

            "cost": ["values"],
            "cooldown": ["values"],
            "damage_type": ""
        }
    ]
}

x = 34e-4
print(x)
b = type(x)

print(b)


class test:
    pass


test1 = test()


}"""



sera = Seraphine(get_dict_champ("Seraphine"), 1000)
ahri = Ahri(get_dict_champ("Ahri"))

ludens = LudensTempest(get_dict_item("6655"))

item_dict_for_champ = {
    "item1": ludens,
    "item2": "",
    "item3": "",
    "item4": "",
    "item5": "",
    "item6": ""
}

sera.set_items_for_champion(item_dict_for_champ)

print(sera.item_dict)

sera.set_base_stats_based_on_level()
sera.set_total_value_to_based_on_level_and_item_stats()


# print(ahri.total_attack_damage)
# print(ahri.auto_attack())
# print(sera.total_attack_damage)
# print(sera.q_ability(700, 0))
# print(sera.auto_attack())
# print(sera.toJSON())
jsonpickle.set_encoder_options('json', indent=4)
test = jsonpickle.encode(sera)

print(test)
