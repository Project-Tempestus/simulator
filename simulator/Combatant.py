from dice_roller import Dice
from .Stats import preset_bonuses, Stats
from .Weapon import Weapon
from .WeaponStats import WeaponStats
from enum import Enum
import numpy as np


class CombatantStatus(Enum):
    OK = 0
    UNCONSCIOUS = 1
    DEAD = 2


class Combatant:
    def __init__(self, stats=Stats, name="John Doe"):
        self.status = CombatantStatus.OK
        self.stats = stats
        self.name = name
        self.initiative = self._set_initiative()
        self.hp_current = self.stats.hp
        self.weapon = Weapon(WeaponStats)
        self.id = 0

    def __str__(self):
        s = f"Combatant  : {self.name}\n"
        s += f"Id         : {self.id}\n"
        s += f"Status     : {self.status}\n"
        s += f"Initiative : {self.initiative}\n"
        s += f"Current HP : {self.hp_current}\n"
        return s

    def set_id(self, id):
        self.id = id

    def _set_initiative(self):
        """
        Roll for initiative: agility + 2d20
        """
        d20 = Dice(20)
        initiative = int(self.stats.agility + d20.roll() + d20.roll())
        print(f"{self.name}:::Initiative = {initiative}")
        return initiative

    def add_bonus(self, bonus):
        """
        Increase or decrease default stats with bonuses
        """
        self.stats.add(bonus)

    def take_wound(self, dmg):
        print(f"{self.name}: took {dmg} wounds.")
        self.hp_current -= dmg

        # TODO: Change with support for unconscious. Currently assumes that 0 HP is death.
        if self.hp_current <= 0:
            self.hp_current = 0
            self.status = CombatantStatus.DEAD

    def test_ability(self, ability_value, n=1):
        """
        TODO: Enable luck and misfortune mechanics
        """
        d100 = Dice(100)
        rolls = d100.generate(n)

        successes = ability_value - rolls
        successes = np.where(successes >= 0)

        print(f"Ability test: {ability_value}")
        print(f"Rolls: {rolls}")
        num_success = len(successes[0])
        print(f"Number succeeded: {num_success}")

        return num_success

    def attack(self):
        print(f"Action: attack by {self.name}")
        n = self.weapon.stats.burst
        dmg = self.weapon.stats.dmg
        attack_ability = self.stats.marksmanship

        hits = self.test_ability(attack_ability, n)
        return ["attack", hits, dmg]

    def aim(self, available_enemies):
        """
        TODO: Enable a more sophisticated approach
        """
        enemy = available_enemies[0]
        print(f"Subaction: taking aim at {enemy.name}")
        return enemy

    def act(self, available_enemies):
        """
        Main AI entrypoint:

        - He can decide whether to reload, shoot, move etc.

        Add world_info, e.g. handles to enemies so that we can decide who to attack
        """
        aim_info = self.aim(available_enemies)
        attack_info = self.attack()
        attack_info.append(aim_info)
        return attack_info


class Guardsman(Combatant):
    def __init__(self, regiment, subclass, name="John Doe"):
        super().__init__(Stats(), name)

        self.add_bonus(preset_bonuses[regiment])
        self.add_bonus(preset_bonuses[subclass])
