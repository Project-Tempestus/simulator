from ..simulator.Simulator import Simulator


def test_simulator():
    sim = Simulator(scenario_file="1v1.yaml")
    sim.run()
