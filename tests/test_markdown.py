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
    basename = "PythonArgmax"

    yaml_path = os.path.join("exercises", basename + ".yaml")
    data_dirpath = os.path.join("tests", "data")

    md_name = basename + ".md"
    md_path = os.path.join(data_dirpath, md_name)
    out_path = os.path.join(out_dirpath, md_name)

    command = ["trafaret", "markdown", yaml_path]
    output_to_file(command, out_path)

    subprocess.check_call(["diff", "-ru", md_path, out_path])
