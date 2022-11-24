from ChampionAbility.Attribute import Attribute

class Effect:
    def __init__(self, attributes: list[Attribute]):
        self.attributes: list[Attribute] = attributes