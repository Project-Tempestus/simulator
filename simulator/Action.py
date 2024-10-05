from enum import Enum
from dataclasses import dataclass
from .Combatant import Combatant


class ActionType(Enum):
    IDLE = 0
    MOVE = 1
    ATTACK = 2


@dataclass
class ActionInfo:
    """
    Type of action, .e.g. "move", "attack"
    Action cost {0,1,2,3}
    """

    type: ActionType = ActionType.IDLE
    cost: int = 0
    initiator: Combatant = Combatant()
    target: Combatant | None = None


@dataclass
class AttackActionInfo(ActionInfo):
    type: ActionType = ActionType.ATTACK


@dataclass
class MoveActionInfo(ActionInfo):
    type: ActionType = ActionType.MOVE
    target: None = None
