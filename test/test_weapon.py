from ..simulator.Weapon import Weapon
from ..simulator.WeaponStats import WeaponStats


def test_weapon():
    weapon = Weapon(WeaponStats())

    for _ in range(5):
        weapon.attack()
    assert weapon.stats.clip_current == 0

    weapon.reload()
    assert weapon.stats.clip_current == weapon.stats.clip_capacity
    print(weapon.stats)
