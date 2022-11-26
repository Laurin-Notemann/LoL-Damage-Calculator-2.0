from Champion.Champion import Champion
from ChampionAbility.ScalingValue import ScalingValue
from ChampionAbility.MissingHealthData import MissingHealthData
from ChampionAbility.Damage import Damage
from ChampionAbility.DamageType import DamageType


class Seraphine(Champion):

    def __init__(self, champ_dict: dict):
        """ Seraphine init:
        echo: increases by 1 everytime she uses an ability, when echo = 3 an ability will be performed twice and set echo = 0
        note_stacks: increases by 1 everytime she uses an ability, max is 4, when she AA she consumes then and deals damage and set note_stacks = 0

        """
        super().__init__(champ_dict)
        self.echo: int = 0
        self.note_stacks: int = 0
        self.missing_health_damage_amplifier: float = 0.05
        self.per_missing_health_percentage: float = 0.075
        self.missing_health_cap: float = 0.75
        # follwing to statements only test purpose
        self.total_ability_power_flat: float = 100
        self.enemy_health = 1000
        self.total_attack_damage = 55
        self.scaling_stats_values: dict[str:ScalingValue] = {
            "AD": ScalingValue("AD", self.total_attack_damage),
            "bonus AD": ScalingValue("bonus AD", self.bonus_attack_damage),
            "AP": ScalingValue("AP", self.total_ability_power_flat)
        }
        self.add_scaling_stats_values_to_ability()

    def increase_note_stacks(self):
        self.note_stacks += 1

    def check_echo(self):
        if self.echo == 3:
            return True
        return False

    def auto_attack(self):
        damage_auto_attack: Damage = Damage(DamageType.PHYSICAL)
        damage_auto_attack.set_damage(self.total_attack_damage)
        if self.note_stacks == 0:
            return damage_auto_attack
        else:
            damage_passive = self.passive_ability()
            return [damage_auto_attack, damage_passive]

    # returns value of the additional damage (only works for the notes she creates by herself so max is 4 currently)
    def passive_ability(self):
        scaled_damage: float = self.total_ability_power_flat * 0.07
        damage: Damage = Damage(DamageType.MAGIC)

        if self.note_stacks > 4:

            self.note_stacks = 4

        if self.champion_level < 6:
            damage.set_damage(round((4 + scaled_damage) * self.note_stacks, 2))
        elif self.champion_level < 11:
            damage.set_damage(round((8 + scaled_damage) * self.note_stacks, 2))
        elif self.champion_level < 16:
            damage.set_damage(round((14 + scaled_damage) * self.note_stacks, 2))
        elif self.champion_level < 19:
            damage.set_damage(round((24 + scaled_damage) * self.note_stacks, 2))

        self.note_stacks = 0
        return damage

    def q_action(self, enemy_current_hp: float = 0, skill_level: int = -1):
        q = self.ability_q[0]
        if q.bounds.lower <= skill_level < q.bounds.upper:
            self.increase_note_stacks()
            missing_health = MissingHealthData(
                self.enemy_health,
                enemy_current_hp,
                self.missing_health_damage_amplifier,
                self.per_missing_health_percentage,
                self.missing_health_cap
            )
            return q.get_damage_based_on_enemy_health(skill_level, 0, missing_health)

    def w_action(self, skill_level=-1):
        return None

    def e_action(self, skill_level=-1):
        e = self.ability_e[0]
        if e.bounds.lower <= skill_level < e.bounds.upper:
            self.increase_note_stacks()
            return e.get_damage(skill_level, 0)

    def r_action(self, skill_level=-1):
        r = self.ability_r[0]
        if r.bounds.lower <= skill_level < r.bounds.upper:
            self.increase_note_stacks()
            return r.get_damage(skill_level, 0)

    def __getstate__(self):
        state = self.__dict__.copy()
        del state["champ_dict"]
        del state["stats"]
        del state["item_dict"]
        del state["echo"]
        del state["note_stacks"]
        return state

    def __setstate__(self, state):
        self.__dict__.update(state)
