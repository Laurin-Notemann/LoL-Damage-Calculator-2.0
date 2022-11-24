from ChampionAbility.Effect import Effect
from ChampionAbility.Attribute import Attribute
from ChampionAbility.ScalingValue import ScalingValue


class Damage:

    # secondary damage only relevant if type = "MIXED_DAMAGE"
    def __init__(self, list_of_effects: list[Effect], list_of_scaling_values: dict[str:ScalingValue], damage_type: str, skill_level: int):
        self.effects = list_of_effects
        self.scaling_values = list_of_scaling_values
        self.type = damage_type
        self.skill_level = skill_level
        self.primary_damage = 0
        self.secondary_damage = 0

    def set_damage(self, damage_type: str, prim_damage: int, sec_damage: int):
        self.type = damage_type
        self.primary_damage = prim_damage
        self.secondary_damage = sec_damage

    def calc_primary_damage(self, effect_number: int, scaling_stats_list: dict[str:ScalingValue]) -> None:
        """
        The damage value in the end depends on multiple different factors but almost every ability has a basic_damage_value,
        which is the first attribute in the in the effects list. To this basic_damage_value we add another value 
        which depends on the current stats of the champion scaled_damage_value, there can be more than one of them, 
        which is why we have list of them.
        """

        base_dmg_attr: Attribute = get_base_attribute(
            self.effects[effect_number])
        scaling_dmg_attributes_dict: dict[str:Attribute] = get_scaling_attributes(
            self.effects[effect_number])
        basic_damage_value = get_flat_value(self.skill_level, base_dmg_attr)
        scaled_damage_values = get_percentage_values(
            self.skill_level,
            scaling_stats_list,
            scaling_dmg_attributes_dict
        )
        print(scaled_damage_values)
        total_damage = basic_damage_value
        for value in scaled_damage_values:
            total_damage += value
        self.primary_damage = total_damage


def get_flat_value(skill_level: int, attribute: Attribute):
    if -1 < skill_level < 6:
        return attribute.values[skill_level]


def get_base_attribute(effect: Effect):
    for attribute in effect.attributes:
        if "" in attribute.unit:
            return attribute


def get_scaling_attributes(effect: Effect):
    scaling_values_dict = {}
    for attribute in effect.attributes:
        if attribute.unit != "":
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