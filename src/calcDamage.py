from Champion.Champion import Champion
from python_champions.Seraphine import Seraphine
from python_champions.Aatrox import Aatrox
from python_champions.Ahri import Ahri
from python_champions.Akali import Akali
from Damage.ScalingValue import ScalingValue
import json

sera_dict = ""
with open(f"/Users/laurin/Documents/PycharmProjects/Playground/LolJsons/current_champions_json/Seraphine.json", "r") as read_file:
    sera_dict = json.load(read_file)
aatrox_dict = ""
with open(f"/Users/laurin/Documents/PycharmProjects/Playground/LolJsons/current_champions_json/Aatrox.json", "r") as read_file:
    aatrox_dict = json.load(read_file)
ahri_dict = ""
with open(f"/Users/laurin/Documents/PycharmProjects/Playground/LolJsons/current_champions_json/Ahri.json", "r") as read_file:
    ahri_dict = json.load(read_file)
akali_dict = ""
with open(f"/Users/laurin/Documents/PycharmProjects/Playground/LolJsons/current_champions_json/Akali.json", "r") as read_file:
    akali_dict = json.load(read_file)


sera: Seraphine = Seraphine(sera_dict)
sera.total_ability_power_flat: float = 100
sera.enemy_health = 1000
sera.total_attack_damage = 55
sera.scaling_stats_values: dict[str:ScalingValue] = {
    "AD": ScalingValue("AD", sera.total_attack_damage),
    "bonus AD": ScalingValue("bonus AD", sera.bonus_attack_damage),
    "AP": ScalingValue("AP", sera.total_ability_power_flat)
}
sera.add_scaling_stats_values_to_ability()

aatrox: Aatrox = Aatrox(aatrox_dict)
aatrox.enemy_health = 1000
aatrox.set_total_value_to_based_on_level_and_item_stats()

akali: Akali = Akali(akali_dict)
akali.enemy_health = 1000
akali.total_ability_power_flat = 100
akali.set_total_value_to_based_on_level_and_item_stats()

ahri: Ahri = Ahri(ahri_dict)
ahri.total_ability_power_flat = 100
ahri.set_total_value_to_based_on_level_and_item_stats()


print("SERAPHINE:")
print(sera.auto_attack().damage)
print(sera.q_action(1000, 2).damage)
print(sera.q_action(1000-140, 2).damage)
print(sera.e_action(1).damage)
print(sera.r_action(0).damage)
print(sera.auto_attack())
print("\n"*5)

print("AATROX:")
print(aatrox.auto_attack()[1].damage)
print(aatrox.q_action(1, True, 0).damage)
print(aatrox.q_action(1, False, 1).damage)
print(aatrox.q_action(1, True, 2).damage)
print(aatrox.w_action(2, True).damage)
print(aatrox.w_action(2, False).damage)
print(aatrox.total_attack_damage)
print(aatrox.r_action(0))
print(aatrox.total_attack_damage)
print(aatrox.auto_attack())
print("\n"*5)

print("AHRI:")
print(ahri.auto_attack().damage)
print(ahri.q_action(2)[1].damage)
print(ahri.q_action(2, False).damage)
print(ahri.w_action(3, 1).damage)
print(ahri.w_action(3, 2))
print(ahri.w_action(3, 3))
print(ahri.e_action(1).damage)
print(ahri.r_action(0, 2)[0].damage)
print("\n"*5)

print("AKALI:")
print(akali.auto_attack().damage)
print(akali.q_action(3).damage)
print(akali.e_action(1, second_instance=False).damage)
print(akali.e_action(1).damage)
print(akali.r_action(0, 600)[1].damage)  # not working second r problems
print(akali.r_action(0, 700, False).damage)
print(akali.r_action(0, 700, second_instance=False).damage)
print(akali.auto_attack())
print("\n"*5)
