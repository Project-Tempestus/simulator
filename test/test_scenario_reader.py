from ..simulator.ScenarioReader import ScenarioReader
from pathlib import Path, WindowsPath
from os.path import dirname, abspath
from ..simulator.Simulator import SYSTEM_CONFIG


def test_scenario_reader():
    f = SYSTEM_CONFIG.scenarios_dir / Path("1v1.yaml")
    print(f)
    reader = ScenarioReader()

    reader.read(f)
