import os
from subprocess import run

import pytest


def build_instances():
    if os.geteuid() != 0:
        pytest.skip(
            "You need to have root privileges to run this script.\nPlease try again, this time using 'sudo'. Exiting."
        )
    run(["singularity", "build", "containers/base.sif containers/base.def"])
    run(["singularity", "build", "containers/runner.sif containers/runner.def"])
