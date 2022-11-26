"""from python_champions.Seraphine import Seraphine
from python_champions.A.Ahri import Ahri
from python_items.L.LudensTempest import LudensTempest
from get_dict import get_json_champ, get_json_item"""
"""
import jsonpickle
"""
"""ability_dict = {
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

"""
"""


sera = Seraphine(get_json_champ("Seraphine"), 1000)
ahri = Ahri(get_json_champ("Ahri"))

ludens = LudensTempest(get_json_item("6655"))

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
test = jsonpickle.encode(sera, unpicklable=False)

print(test)


json_dict = {
    "selected_champ": "name_of_champ",
    "selected_items": ["name_of_item1", "name_of_item2", ".."],
    "selected_actions": ["name_of_action1", "name_of_action2", ".."],
    "champ_level": 1,
    "ability_level": ["qlevel_number", "wlevel_number", ".."],
    "dummy": {
        "hp": 0,
        "armor": 0,
        "magic_res": 0
    }
}

return_dict = {
    "champ_with_new_stats": "champModel",
    "damageoutput": ["total", "true", "physic", "magic"],
    "damage_of_abilities": {
        "actionNumber": "damagenumber"
    }
}"""
test_data = {
    "abilityLevel": [1, 3, 4, 2],
    "championLevel": 8,
    "listOfItemIDs": [0, 6653, 0, 6655, 0, 0],
    "dummyStats": [1000, 0, 0],
    "championID": 147,
    "listOfActionNames": ["Q", "Q", "AA", "W", "E", "R"]
}

for i in range(1, 19, 5):
    print(i)

a = [1, 2]
b = [1]

print(len(a))
print(len(b))


def test(*args):
    print(type(args))


test(1, 2, 3, 4)


t = "% AP"

print(t[2:])

a = []
print(len(a))

