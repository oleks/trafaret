import os.path
import subprocess
import pytest

from typing import List
from _pytest.tmpdir import TempdirFactory


@pytest.fixture(scope='session')
def out_dirpath(tmpdir_factory: TempdirFactory) -> str:
    return str(tmpdir_factory.mktemp('trafaret'))


def output_to_file(command: List[str], path: str) -> None:
    with open(path, 'w') as f:
        f.write(subprocess.check_output(command).decode('utf-8'))


def test_solution(out_dirpath: str) -> None:
    basename = "PythonArgmax"

    yaml_path = os.path.join("exercises", basename + ".yaml")
    data_dirpath = os.path.join("tests", "data")

    txt_name = basename + ".solutions.txt"
    txt_path = os.path.join(data_dirpath, txt_name)
    out_path = os.path.join(out_dirpath, txt_name)

    command = ["trafaret", "solution", yaml_path]
    output_to_file(command, out_path)

    subprocess.check_call(["diff", "-ru", txt_path, out_path])