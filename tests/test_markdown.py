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


def test_show(out_dirpath: str) -> None:
    yaml_path = os.path.join("exercises", "PythonMax.yaml")
    data_dirpath = os.path.join("tests", "data")

    md_path = os.path.join(data_dirpath, "PythonMax.md")
    out_path = os.path.join(out_dirpath, "PythonMax.md")

    command = ["trafaret", "markdown", yaml_path]
    output_to_file(command, out_path)

    subprocess.check_call(["diff", "-ru", md_path, out_path])
