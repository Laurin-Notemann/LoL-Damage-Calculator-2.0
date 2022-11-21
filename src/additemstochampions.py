from python_champions.index import list_of_py_champs
from python_items.index import list_of_py_items
from python_champions.Champion import Champion

test_dict = {
    "abilityLevel": [1, 3, 4, 2],
    "championLevel": 8,
    "listOfItemIDs": [0, 6653, 0, 6655, 0, 0],
    "dummyStats": [1000, 0, 0],
    "championID": 147,
    "listOfActionNames": ["Q", "Q", "AA", "W", "E", "R"]
}


def update_champion(data: dict):
    chosen_champ: Champion = find_champion_in_list(data["championID"])
    assign_items_to_champ(data["listOfItemIDs"], chosen_champ)
    set_champion_stats(
        chosen_champ,
        data["championLevel"],
        data["dummyStats"][0])
    # print(chosen_champ.champion_name, chosen_champ.item_dict, chosen_champ.champion_level, chosen_champ.enemy_health)


def find_champion_in_list(champ_id: int):
    # print(list_of_champs)
    for champ in list_of_py_champs:
        if champ.champion_id == champ_id:
            return champ


def assign_items_to_champ(item_id_list: list, chosen_champ: Champion):
    list_of_chosen_items = []
    for item_id in item_id_list:
        if item_id != 0:
            for item in list_of_py_items:
                if item_id == item.item_id:
                    list_of_chosen_items.append(item)
        else:
            list_of_chosen_items.append(None)

    for item_index in range(1, len(list_of_chosen_items)+1):
        chosen_champ.item_dict[f"item{item_index}"] = list_of_chosen_items[item_index-1]


def set_champion_stats(champion: Champion, level: int, enemy_health: int):
    champion.set_champion_level(level)
    champion.set_enemy_health(enemy_health)
