from subprocess import run


def test_instances():
    # Execute the runner
    result = run(
        [
            "singularity",
            "run",
            "--userns",
            "--writable",
            "--app",
            "test",
            "containers/runner.sif",
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
