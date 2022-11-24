from ChampionAbility.Attribute import Attribute

class ScalingValue:
    def __init__(self, stat_name: str, stat_value: float):
        self.stat_name = stat_name
        self.value = stat_value
        

    def additional_scaled_value(self, skill_level: int, attribute: Attribute):
        return (attribute.values[skill_level]/100) * self.value