from ..simulator.Scenario import Scenario, Team
from ..simulator.Combatant import Combatant


def test_scenario():
    english_team = Team(
        "The English",
        combatants=[
            Combatant(name="Johnny John"),
            Combatant(name="Aston Bentley"),
            Combatant(name="Sir Sirsky"),
        ],
    )
    french_team = Team(
        "The French",
        combatants=[
            Combatant(name="Hon Honhon"),
            Combatant(name="Le Baguette"),
            Combatant(name="Rocquefort Bordeaux"),
        ],
    )
    scenario = Scenario(name="Battle of Agincourt", teams=[english_team, french_team])
    print(scenario)
    free_id = scenario.get_free_id()
    print(f"free_id = {free_id}")
