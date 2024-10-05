from dataclasses import dataclass
from .Combatant import Combatant
from .Combatant import CombatantStatus
from .Stats import Stats
from typing import List, Dict
import collections


@dataclass
class Team:
    name: str
    combatants: List[Combatant]

    def get_free_id(self):
        ids = []
        for c in self.combatants:
            ids.append(c.id)
        return max(ids) + 1

    def __str__(self):
        s = f"Team: {self.name}\n"
        for c in self.combatants:
            s += str(c)
        return s


class Scenario:

    def __init__(self, name: str, teams: List[Team]):
        self.name = name
        self.teams = teams
        self._set_ids()

    def __str__(self):
        s = f"Scenario: {self.name}\n"
        for team in self.teams:
            s += str(team)
        return s

    def get_free_id(self):
        free_ids = []
        for team in self.teams:
            free_ids.append(team.get_free_id())
        return max(free_ids)

    def _set_ids(self):
        for team in self.teams:
            for c in team.combatants:
                c.set_id(self.get_free_id())

    # def get_round_q(self):
    #     """
    #     Returns turn order q in order of initiative.
    #     Currently does not account for tie-breakers.
    #     Filters out not-OK combatants.
    #     Always use:
    #     * `append` to add element to the right
    #     * `popleft` to remove elements from the left
    #     TODO: Divide this function into smaller, reusable functions?
    #     """
    #     all_combatants = []
    #     for team in self.teams:
    #         for c in team.combatants:
    #             if c.status == CombatantStatus.OK:
    #                 all_combatants.append([c, c.initiative])

    #     def sort_key(row):
    #         return row[1]

    #     all_combatants.sort(key=sort_key, reverse=True)

    #     sorted_combatants = []
    #     for row in all_combatants:
    #         sorted_combatants.append(row[0])

    #     round_q = collections.deque(sorted_combatants)

    #     return round_q
