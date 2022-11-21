import json


def get_ability_values(key: str, champ_dict: dict):
    ability_values = get_abilities_data(champ_dict["abilities"][key])

    return {key: ability_values}


def get_abilities_data(list_of_ability_dicts: dict):
    """
    Get all the ability data from the champion 
    """

    temp_list = []
    for ability_number in range(len(list_of_ability_dicts)):
        ability_dict = {}

        ability_dict = get_ability_effects(
            list_of_ability_dicts[ability_number]["effects"])

        ability_dict["cost"] = get_ability_costs(
            list_of_ability_dicts[ability_number]["cost"]["modifiers"])

        ability_dict["cooldown"] = get_ability_cooldowns(
            list_of_ability_dicts[ability_number]["cooldown"]["modifiers"])

        ability_dict["damage_type"] = list_of_ability_dicts[ability_number]["damageType"]

        temp_list.append(ability_dict)

    return temp_list


def get_ability_effects(list_of_effect_dicts: list):
    effects_dict = {}
    for effect_number in range(len(list_of_effect_dicts)):
        temp_dict = get__effect_attributes(
            list_of_effect_dicts[effect_number]["leveling"])
        if temp_dict:
            effects_dict[f"effect{effect_number}"] = temp_dict
    return effects_dict


def get__effect_attributes(list_of_attribute_dicts: list):
    attributes_dict = {}
    for attribute_number in range(len(list_of_attribute_dicts)):
        temp_list = get_attribute_modifiers(
            list_of_attribute_dicts[attribute_number]["modifiers"])
        attributes_dict[f"attribute{attribute_number}"] = temp_list
    return attributes_dict


def get_attribute_modifiers(list_of_modifier_dicts: dict):
    modifier_list = []
    for modifier_number in range(len(list_of_modifier_dicts)):
        effect_mod_values: list = list_of_modifier_dicts[modifier_number]["values"]
        effect_mod_unit: list = list_of_modifier_dicts[modifier_number]["units"]
        modifier_list.append([effect_mod_values, effect_mod_unit])
    return modifier_list


def get_ability_costs(cost_list: list):
    if cost_list is not None:
        return cost_list[0]["values"]


def get_ability_cooldowns(cooldown_list: list):
    if cooldown_list is not None:
        return cooldown_list[0]["values"]


test = ""
with open(f"Seraphine.json", "r") as read_file:
    test = json.load(read_file)

print(get_ability_values("Q", test))
