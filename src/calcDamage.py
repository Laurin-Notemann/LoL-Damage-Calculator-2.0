from Champion.Champion import Champion
from python_champions.Seraphine import Seraphine
import json

test = ""
with open(f"/Users/laurin/Documents/PycharmProjects/Playground/LolJsons/src/Seraphine.json", "r") as read_file:
    test = json.load(read_file)

sera: Seraphine = Seraphine(test)



# print(sera.ability_e[0].effects[0].attributes)
print(sera.test_e_ability(2).type)
