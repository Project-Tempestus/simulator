from ..simulator.Combatant import Combatant, Guardsman, CombatantStatus
from ..simulator.Stats import Stats


def test_combatant():
    _ = Combatant(stats=Stats)
    guardsman = Guardsman(name="Dora", regiment="krieg", subclass="stm")

    print(guardsman.stats)

    guardsman.take_wound(dmg=20)
    guardsman.take_wound(dmg=100)
    guardsman.take_wound(dmg=100)
    print(guardsman)

    assert guardsman.hp_current == 0
    assert guardsman.status == CombatantStatus.DEAD


def test_rolls():
    guardsman = Guardsman(name="Dora", regiment="krieg", subclass="stm")

    print(guardsman.stats)

    guardsman.test_ability(guardsman.stats.strength)
    guardsman.test_ability(guardsman.stats.marksmanship, n=guardsman.weapon.stats.burst)
