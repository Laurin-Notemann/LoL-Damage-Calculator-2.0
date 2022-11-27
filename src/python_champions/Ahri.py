from Champion.Champion import Champion
from ChampionAbility.Ability import Ability
from ChampionAbility.Damage import Damage


class Ahri(Champion):
    def __init__(self, champ_dict):
        super().__init__(champ_dict)

    def passive_ability(self):
        pass

    def q_action(self, skill_level: int=-1, first_pass: bool=True, last_pass: bool=True):
        q: Ability = self.ability_q[0]
        if self.skill_level_inside_bounds(skill_level, q):
            damage_first_pass: Damage = q.get_damage(skill_level, 0)
            damage_second_pass: Damage = q.get_damage(skill_level, 0)
            if first_pass and last_pass:
                return [damage_first_pass, damage_second_pass]
            elif first_pass:
                return damage_first_pass
            elif last_pass:
                return damage_second_pass

    def w_action(self, skill_level: int=-1, amount_hit: int=3):
        w: Ability = self.ability_w[0]
        if self.skill_level_inside_bounds(skill_level, w):
            first_hit: Damage = w.get_damage(skill_level, 1)
            subsequent_hit: Damage = w.get_damage(skill_level, 2)
            if amount_hit == 1:
                return first_hit
            elif amount_hit == 2:
                return [first_hit, subsequent_hit]
            elif amount_hit == 3:
                return [first_hit, subsequent_hit, subsequent_hit]

    def e_action(self, skill_level: int=-1):
        e: Ability = self.ability_e[0]
        if self.skill_level_inside_bounds[skill_level, e]:
            return e.get_damage(skill_level, 0)

    def r_action(self, skill_level: int=-1, amount_used: int=1):
        r: Ability = self.ability_r[0]
        if self.skill_level_inside_bounds(skill_level, r):
            r_damage: Damage = r.get_damage(skill_level, 0)
            list_of_amount_of_r: list[Damage]= []
            for i in range(amount_used):
                list_of_amount_of_r.append(r_damage)
            return list_of_amount_of_r
