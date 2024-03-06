from subprocess import run

from utils_test import get_config


def test_instances():
    GH_HOSTNAME, GH_ORG, GH_PERSONAL_TOKEN = get_config()

    # Execute the runner
    result = run(
        [
            "timeout",
            "10s",
            "singularity",
            "run",
            "--env",
            f"GH_HOSTNAME={GH_HOSTNAME},GH_ORG={GH_ORG}",
            "--userns",
            "--writable",
            "containers/runner.sif",
            GH_PERSONAL_TOKEN,
        ],
        capture_output=True,
        text=True,
    )

    print(result.stdout)
    assert "Runner successfully added" in result.stdout


if __name__ == "__main__":
    test_instances()
