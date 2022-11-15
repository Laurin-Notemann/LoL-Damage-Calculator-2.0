import json




def get_dict_champ(champion_name: str):
    with open(f"current_champions_json/{champion_name}.json", "r") as read_file:
        return json.load(read_file)

def get_dict_item(champion_name: str):
    with open(f"current_items_json/{champion_name}.json", "r") as read_file:
        return json.load(read_file)

"""
# hmm
def test_champ(champ: Champion):
    print([champ.q_ability(1), champ.w_ability(1), champ.e_ability(1), champ.r_ability(1)])
"""