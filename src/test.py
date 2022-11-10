from python_champions.Seraphine import Seraphine
from python_champions.Ahri import Ahri
from python_champions.get_dict import get_dict

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

item_dict = {
    "item1": test1,
    "item2": "",
    "item3": "",
    "item4": "",
    "item5": "",
    "item6": ""
}"""

sera = Seraphine.Seraphine(get_dict("Seraphine"), 1000)
ahri = Ahri.Ahri(get_dict("Ahri"))

print(ahri.total_attack_damage)
print(ahri.auto_attack())
print(sera.total_attack_damage)
print(sera.q_ability(700, 0))
print(sera.auto_attack())
# print(sera.toJSON())
jsonpickle.set_encoder_options('json', sort_keys=True, indent=4)
test = jsonpickle.encode(sera)

# print(test)
