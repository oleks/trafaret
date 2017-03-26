#!/usr/bin/env python3

import subprocess
import sys
from typing import List

exitcode = 0


def run(command: List[str]) -> None:
    global exitcode
    try:
        subprocess.check_call(command)
    except subprocess.CalledProcessError:
        exitcode = 1


files = ["static_tests.py", "trafaret", "tests"]

run(["flake8"] + files)
run([
        "mypy",
        "--disallow-untyped-calls",
        "--disallow-untyped-defs",
        "--strict-optional",
        "--ignore-missing-imports"
    ] + files)

sys.exit(exitcode)
