import json


def get_json_champ(champion_name: str):
    with open(f"current_champions_json/{champion_name}.json", "r") as read_file:
        return json.load(read_file)


def get_json_item(champion_name: str):
    with open(f"current_items_json/{champion_name}.json", "r") as read_file:
        return json.load(read_file)
