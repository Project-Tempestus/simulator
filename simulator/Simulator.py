from dataclasses import dataclass
from .Combatant import Combatant, CombatantStatus
from .Stats import Stats
from .ScenarioReader import ScenarioReader
import collections
from pathlib import Path
from os.path import dirname, abspath


@dataclass
class SystemConfig:
    """
    Global configuration
    """

    actions_per_round: int = 3
    scenarios_dir: Path = dirname(dirname(abspath(__file__))) / Path("data")


SYSTEM_CONFIG = SystemConfig()


class Simulator:
    """
    TODO: Enable more than 2 teams, there is some basic infra for it, but the run function will ignore more than 2 teams?
    TODO: Enable bleeding and status effects on combatants
    """

    def __init__(self, scenario_file) -> None:
        self.scenario_reader = ScenarioReader()
        scenario_path = SYSTEM_CONFIG.scenarios_dir / scenario_file
        self.scenario = self.scenario_reader.read(scenario_path)
        """
            Always use append to add element to the right
            and popleft to remove elements from the left
        """

    def run(self):
        """
        1. Establish initiative
        2. In order of initiative:
            a. Issue action to the Combatant
            b. Resolve notifications from this Combatant

        """

        # FIXME: Hard set to 3 rounds, regardless if anyone is alive
        for round_number in range(1000):
            print("")
            print(f"Round: {round_number+1}")

            if round_number == 5:
                break
            # We rely on the fact that get_round_q returns a sorted list of OK combatants
            # self.q_round = self.scenario.get_round_q()

            # # Process current combatant
            # current_combatant = self.q_round.popleft()
            # print(f"Turn: {current_combatant}")
            # # We assume that everyone is in weapon's range and there is no movement

            # # Give turn to current_combatant
            # # He decides what action to take
            # # He returns object of type Interaction
            # # Interaction:
            # #   type
            # #   success
            # #   metadata dependent on type: number of attacks

            # # FIXME: Currently will always attack 1st combatant of first team (can be self)
            # available_enemies = self.scenario.teams[0].combatants

            # # process each action
            # # while not used 3 actions:
            # act_info = current_combatant.act(available_enemies)
            # print(f"act_info: {act_info}")

            # # We adjust the world based on the type of the interaction
            # # Move objects, deal wounds, etc.

            # if act_info[0] == "attack":
            #     dmg = act_info[1] * act_info[2]
            #     act_info[3].take_wound(dmg)

            # if (available_enemies[0]).status == CombatantStatus.DEAD:
            #     print("Someone died.")
            #     print(f"Finishing simulation after {round_number} rounds.")
            #     break
