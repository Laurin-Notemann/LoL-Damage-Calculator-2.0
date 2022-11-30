from ChampionAbility.Effect import Effect
from ChampionAbility.Attribute import Attribute
from Damage.ScalingValue import ScalingValue
from Utilities.DamageUtils.dmgValues import get_flat_value, get_base_attribute, get_scaling_attributes, get_percentage_values


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

