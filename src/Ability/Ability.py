from Bounds import Bounds
from Effect import Effect


class Ability:
    def __init__(self, id_name: str, full_name: str, bounds: Bounds, effects: list[Effect], costs: list[int], cooldowns: list[int], damage_type: str):
        self.id_name: str = id_name
        self.full_name: str = full_name
        self.lower_bound: int = bounds.lower
        self.upper_bound: int = bounds.upper
        self.effects = effects
        self.costs = costs
        self.cooldowns = cooldowns
        self.damage_type = damage_type

    def damage(self):
        pass

    def shield(self):
        pass

    def heal(self):
        pass

    def damage_reduction(self):
        pass

    def level_scaling_damage(self, champion_level, increment_param):
        min_level = 1
        max_level = 19
        for i in range(min_level, max_level, increment_param):
            if champion_level == i:
                pass

    def regular_damage(self, curr_level: int,  base_func,  extra_func=None, effect_number: int = 0, attribute_number: int = 0, scaling_param: str = ""):
        if self.lower_bound - 1 < curr_level < self.upper_bound + 1:
            if extra_func:
                extra_func()
            return base_func(self.id_name, curr_level, effect_number, attribute_number, scaling_param)
