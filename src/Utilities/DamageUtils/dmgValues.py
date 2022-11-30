from ChampionAbility.Effect import Effect
from ChampionAbility.Attribute import Attribute
from Damage.ScalingValue import ScalingValue


def get_flat_value(skill_level: int, attribute: Attribute):
    return attribute.values[skill_level]


def get_base_attribute(effect: Effect, attribute_num):
    for attribute in effect.attributes[attribute_num]:
        if "" in attribute.unit:
            return attribute


def get_scaling_attributes(effect: Effect, attribute_num):
    scaling_values_dict = {}
    for attribute in effect.attributes[attribute_num]:
        if attribute.unit[0] != "" and attribute.unit[0][2:] != "":
            scaling_values_dict[attribute.unit[0][2:]] = attribute
    return scaling_values_dict


def get_percentage_values(skill_level: int, scaling_stats: dict[str:ScalingValue], scaling_dmg_attr_dict: dict[str:Attribute]):
    list_of_dmg_values = []
    for key, value in scaling_dmg_attr_dict.items():
        if key in scaling_stats:
            # print(scaling_stats[key], value)
            list_of_dmg_values.append(calc_damage_value(
                scaling_stats[key].value,
                value.values[skill_level])
            )
    return list_of_dmg_values


def calc_damage_value(champion_stat: float, scaling_value: int):
    return ((scaling_value/100) * champion_stat)
