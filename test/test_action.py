from ..simulator.Action import ActionInfo, AttackActionInfo, MoveActionInfo


def test_action():
    action_info = ActionInfo()
    print(action_info)

    attack_info = AttackActionInfo()
    print(attack_info)

    move_info = MoveActionInfo()
    print(move_info)
