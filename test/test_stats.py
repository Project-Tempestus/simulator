from ..simulator.Stats import Stats
from ..simulator.Stats import preset_bonuses


def test_combatant():
    golden_cadia = Stats(
        marksmanship=20,
        cqb=45,
        strength=40,
        constitution=45,
        agility=45,
        knowledge=30,
        hp=100,
    )

    stats = Stats()
    bonus = preset_bonuses["cadia"]
    stats.add(bonus)

    assert stats == golden_cadia
