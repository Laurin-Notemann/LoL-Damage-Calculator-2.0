ability_dict = {
    "Q": [
        {
            "effects1": {
                "attribute1": [
                    ["values", "unit"], ["values", "unit"], ["values", "unit"]
                ],
                "attribute2": [
                    ["values", "unit"]
                ],
                "attribute3": [
                    ["values", "unit"], ["values", "unit"]
                ]
            },
            "effects2": {
                "attribute1": [
                    ["values", "unit"], ["values", "unit"]
                ],
                "attribute2": [
                    ["values", "unit"], ["values", "unit"]
                ]
            },

            "cost": ["values"],
            "cooldown": ["values"],
            "damage_type": ""
        }
    ]
}


def get_amp_based_on_missing_health(enemy_missing_health_perc, missing_health_iterator_static, damage_amplifier_missing_health_static,
                                    missing_health_cap):
    missing_health_iterator = missing_health_iterator_static
    damage_amplifier_missing_health = damage_amplifier_missing_health_static
    for i in range(0, int((missing_health_cap / missing_health_iterator)) + 1):
        if enemy_missing_health_perc < missing_health_iterator_static:
            damage_amplifier_missing_health = 0
            break
        elif missing_health_iterator < enemy_missing_health_perc < (
                missing_health_iterator + missing_health_iterator_static) or enemy_missing_health_perc == missing_health_iterator:
            break
        missing_health_iterator = round(missing_health_iterator + missing_health_iterator_static, 5)
        damage_amplifier_missing_health = round(damage_amplifier_missing_health + damage_amplifier_missing_health_static, 5)

    return damage_amplifier_missing_health


print(get_amp_based_on_missing_health(0.56, 0.01, 0.0286, 0.7))
print(get_amp_based_on_missing_health(0.75, 0.0003, 0.0002, 0.75))
