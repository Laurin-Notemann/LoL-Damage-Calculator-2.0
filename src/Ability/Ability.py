from Ability.Bounds import Bounds

class Ability:
    def __init__(self, id_name: str, full_name: str, bounds: Bounds, base_func, effect_number: int = 0, attribute_number: int = 0, scaling_param: str = "", extra_func=None):
        self.id_name = id_name
        self.full_name = full_name
        self.lower_bound = bounds.lower
        self.upper_bound = bounds.upper
        self.base_func = base_func
        self.extra_func = extra_func
        self.effect_number = effect_number
        self.attribute_number = attribute_number
        self.scaling_param = scaling_param

    def level_scaling_damage(self, champion_level, increment_param):
        min_level = 1
        max_level = 19
        for i in range(min_level, max_level, increment_param):
            if champion_level == i:
                pass

    def regular_damage(self, curr_level: int):
        if self.lower_bound - 1 < curr_level < self.upper_bound + 1:
            if self.extra_func:
                self.extra_func()
            return self.base_func(self.id_name, curr_level, self.effect_number, self.attribute_number, self.scaling_param)
