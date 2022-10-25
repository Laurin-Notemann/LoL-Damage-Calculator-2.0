import json

from Champion import Champion


def get_dict(champion_name: str):
    with open(f"{champion_name}.json", "r") as read_file:
        return json.load(read_file)

# hmm
def test_champ(champ: Champion):
    print([champ.q_ability(1), champ.w_ability(1), champ.e_ability(1), champ.r_ability(1)])
