from ChampionAbility.Effect import Effect
from ChampionAbility.Attribute import Attribute
from ChampionAbility.ScalingValue import ScalingValue
from ChampionAbility.Bounds import Bounds


class Damage:

    def __init__(self, damage_type: str):
        self.damage_type: str = damage_type
        self.damage: float = 0

    # Used if the damage values are not inside of the champion json.
    def set_damage(self, damage: float):
        self.damage = damage

    def set_damage_type(self, damage_type: str):
        self.damage_type = damage_type
    
    def calc_damage(self, effect: Effect, scaling_values: dict[str:ScalingValue], skill_level: int, attribute_num: int = 0) -> None:
        """
        The damage value in the end depends on multiple different factors but almost every ability has a basic_damage_value,
        which is the first attribute in the in the effects list. To this basic_damage_value we add another value 
        which depends on the current stats of the champion scaled_damage_value, there can be more than one of them, 
        which is why we have list of them.
        """

        base_dmg_attr: Attribute = get_base_attribute(effect, attribute_num)
        scaling_dmg_attributes_dict: dict[str:Attribute] = get_scaling_attributes(
            effect,
            attribute_num)
        basic_damage_value: float = get_flat_value(skill_level, base_dmg_attr)
        scaled_damage_values: float = get_percentage_values(skill_level,
                                                            scaling_values,
                                                            scaling_dmg_attributes_dict
                                                            )
        total_damage: float = basic_damage_value
        for value in scaled_damage_values:
            total_damage += value
        self.set_damage(round(total_damage, 2))


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
