from Champion.Champion import Champion
from python_champions.Seraphine import Seraphine
import json

test = ""
with open(f"/Users/laurin/Documents/PycharmProjects/Playground/LolJsons/current_champions_json/Seraphine.json", "r") as read_file:
    test = json.load(read_file)
sera: Seraphine = Seraphine(test)

print(sera.auto_attack().damage)
print(sera.q_action(1000, 2).damage)
print(sera.q_action(1000-140, 2).damage)
print(sera.e_action(1).damage)
print(sera.r_action(0).damage)
print(sera.auto_attack)

