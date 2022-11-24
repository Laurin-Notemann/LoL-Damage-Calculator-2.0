from ChampionAbility.Bounds import Bounds
from ChampionAbility.Effect import Effect
from ChampionAbility.Damage import Damage
from ChampionAbility.ScalingValue import ScalingValue

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

    def get_dmg(self, skill_level: int, scaling_values: dict[str:ScalingValue], effect_number: int):
        damage = Damage(self.effects, scaling_values, self.damage_type, skill_level)
        if self.damage_type == "MIXED_DAMAGE":
            pass
        damage.calc_primary_damage(effect_number, scaling_values)
        return damage

    def damage(self):
        pass
    

    def shield(self):
        pass
        

    def heal(self):
        pass

    def damage_reduction(self):
        pass