from ChampionAbility.Bounds import Bounds
from ChampionAbility.Effect import Effect
from Damage.Damage import Damage
from Damage.ScalingValue import ScalingValue
from Damage.MissingHealthData import MissingHealthData


class Ability:
    def __init__(self, id_name: str, full_name: str, bounds: Bounds, effects: list[Effect], costs: list[int], cooldowns: list[int], damage_type: str):
        self.id_name: str = id_name
        self.full_name: str = full_name
        self.bounds: Bounds = bounds
        self.effects: list[Effect] = effects
        self.costs: list[int] = costs
        self.cooldowns: list[int] = cooldowns
        self.damage_type: str = damage_type
        self.scaling_values: dict[str:ScalingValue] = {}

    def set_scaling_values(self, scaling_stats_values: dict[str:ScalingValue]):
        self.scaling_values = scaling_stats_values

    # effect_number and attribute_num default 0 because most abilites use the first effect and first attribute
    def get_damage(self, skill_level: int, effect_number: int = 0, attribute_num: int = 0):
        damage = Damage(self.damage_type)
        damage.calc_damage(
            self.effects[effect_number],
            self.scaling_values,
            skill_level, attribute_num)
        return damage

    def get_damage_based_on_enemy_health(self, skill_level: int, missing_health: MissingHealthData, effect_number: int = 0, attribute_num: int = 0):
        damage = self.get_damage(skill_level, effect_number, attribute_num)
        temp = damage.damage
        temp += temp * missing_health.amplifier
        damage.set_damage(round(temp, 2))
        return damage

    def shield(self):
        pass

    def heal(self):
        pass

    def damage_reduction(self):
        pass
