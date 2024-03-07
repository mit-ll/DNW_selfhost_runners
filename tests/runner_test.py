from subprocess import run

from utils_test import get_config


def test_instances():
    GH_HOSTNAME, GH_ORG, GH_PERSONAL_TOKEN = get_config()

    # Execute the runner
    result = run(
        [
            "singularity",
            "run",
            "--env",
            f"GH_HOSTNAME={GH_HOSTNAME},GH_ORG={GH_ORG}",
            "--userns",
            "--writable",
            "--app",
            "test_runner",
            "containers/runner.sif",
            GH_PERSONAL_TOKEN,
        ],
        capture_output=True,
        text=True,
    )

    print(result.stdout)

    # Verify messages
    assert "Connected to GitHub" in result.stdout
    assert "Runner successfully added" in result.stdout
    assert "Runner connection is good" in result.stdout
    assert "Runner removed successfully" in result.stdout


if __name__ == "__main__":
    test_instances()
