import os

import typer


def get_config():
    # Verify variables are set
    gh_hostname = os.environ.get("GH_HOSTNAME", None)
    gh_org = os.environ.get("GH_ORG", None)

    if gh_hostname is None:
        print("Environment varible GH_HOSTNAME must be set")
        print("$ export GH_HOSTNAME=<github.com>")
        raise ValueError("Invalid value")
    if gh_org is None:
        print("Environment varible GH_ORG must be set")
        print("$ export GH_ORG=<my-organization>")
        raise ValueError("Invalid value")

    # Get secret from user
    print("\n" + "-" * 50)
    print(f"GH_HOSTNAME={gh_hostname}")
    print(f"GH_ORG={gh_org}")
    gh_personal_token = typer.prompt("What's your Github Personal token?")
    print("-" * 50)

    return gh_hostname, gh_org, gh_personal_token
