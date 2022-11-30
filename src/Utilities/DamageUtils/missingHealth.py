def get_enemy_missing_health(enemy_max_hp: float, enemy_current_hp: float):
    return round((enemy_max_hp - enemy_current_hp) / enemy_max_hp, 6)


def get_amp_based_on_missing_health(enemy_missing_health_perc,  damage_amplifier_missing_health_static, missing_health_iterator_static,
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
        missing_health_iterator = round(
            missing_health_iterator + missing_health_iterator_static, 5)
        damage_amplifier_missing_health = round(
            damage_amplifier_missing_health + damage_amplifier_missing_health_static, 5)

    return damage_amplifier_missing_health
