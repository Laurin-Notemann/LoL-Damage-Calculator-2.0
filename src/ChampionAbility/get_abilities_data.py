import json
from ChampionAbility.Attribute import Attribute
from ChampionAbility.Effect import Effect
from ChampionAbility.Ability import Ability
from ChampionAbility.Bounds import Bounds


def get_abilities_data(key: str, champ_dict: dict, bounds: Bounds):
    """
    Get all the static ability data from the champios json files

    We get a list of abilites back because a few champions have two seperate abilities on one key. 
    Most of the time we will only have one entry in the list.
    """

    list_of_ability_dicts = champ_dict["abilities"][key]
    ability_list: list[Ability] = []
    
    for ability_number in range(len(list_of_ability_dicts)):
        curr_dict = list_of_ability_dicts[ability_number]

        effect_list = get_ability_effects(curr_dict["effects"])
        costs = get_ability_costs(curr_dict["cost"])
        cooldowns = get_ability_cooldowns(curr_dict["cooldown"]["modifiers"])
        damage_type = curr_dict["damageType"]

        ability = Ability(
            key, curr_dict["name"], bounds, effect_list, costs, cooldowns, damage_type)

        ability_list.append(ability)

    return ability_list


def get_ability_effects(list_of_effect_dicts: list):
    effects_list = []
    for effect_number in range(len(list_of_effect_dicts)):
        curr_dict = list_of_effect_dicts[effect_number]

        temp_effect = Effect(get_effect_attributes(curr_dict["leveling"]))
        
        effects_list.append(temp_effect)

    return effects_list


def get_effect_attributes(list_of_attribute_dicts: list):
    attributes_list = []
    for attribute_number in range(len(list_of_attribute_dicts)):
        curr_dict = list_of_attribute_dicts[attribute_number]

        attributes_list.append(get_attribute_modifiers(curr_dict["modifiers"]))

    return attributes_list


def get_attribute_modifiers(list_of_modifier_dicts: dict):
    modifier_list = []
    for modifier_number in range(len(list_of_modifier_dicts)):
        curr_dict = list_of_modifier_dicts[modifier_number]

        values: list = curr_dict["values"]
        unit: list = curr_dict["units"]
        modifier_list.append(Attribute(values, unit))

    return modifier_list


def get_ability_costs(cost_list: list):
    if cost_list is not None:
        return cost_list["modifiers"][0]["values"]


def get_ability_cooldowns(cooldown_list: list):
    if cooldown_list is not None:
        return cooldown_list[0]["values"]
"""

test = ""
with open(f"Aatrox.json", "r") as read_file:
    test = json.load(read_file)

test_list: list[Ability] = get_abilities_data("Q", test, Bounds(0, 5))

# print(test_list[0].effects[0].attributes[0][0].values)

print(test_list[0].effects[0].attributes[3].values)"""