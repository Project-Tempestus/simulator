import yaml
from .Combatant import Combatant
from .Stats import Stats
from .Scenario import Team, Scenario
from ..simulator.Stats import preset_bonuses

SUBCLASS_LOOKUP = {
    "chirurgeon": "chr",
    "engineer": "eng",
    "grenadier": "grd",
    "sargeant": "srg",
    "scout": "sct",
    "marksman": "mrk",
    "stormtrooper": "stm",
}


class ScenarioReader:

    def __init__(self) -> None:
        self.scenario = None

    def read(self, file_path):
        """
        TODO: Break this function down into smaller pieces

        1. Reads YAML file
        2. Parses contents into Scenario object
        3. Adds stats to each combatant based on regiment/subclass tags
        """
        with open(file_path, "r") as f:
            f_contents = yaml.safe_load(f)

        print(f"{f_contents}")

        name = f_contents["scenario"]

        teams_container = f_contents["teams"]

        teams_fmt = []
        for team in teams_container:
            team_name = team[0]["name"]
            print(team_name)

            team_combatants = team[1]["combatants"]
            combatants = []
            for c in team_combatants:
                c_name = c["name"]

                # TODO: Better name sanitization
                c_regiment = (c["regiment"]).lower()

                c_subclass = c["subclass"].lower()
                c_subclass = SUBCLASS_LOOKUP[c_subclass]

                # Modify stats
                stats = Stats()
                regiment_bonus = preset_bonuses[c_regiment]
                stats.add(regiment_bonus)
                subclass_bonus = preset_bonuses[c_subclass]
                stats.add(subclass_bonus)

                combatants.append(Combatant(stats=stats, name=c_name))
            teams_fmt.append(Team(team_name, combatants))
        scenario = Scenario(name, teams_fmt)
        print(scenario)
