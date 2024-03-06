import os

import typer


def get_config():
    # Verify variables are set
    gh_hostname = os.environ.get("GH_HOSTNAME", None)
    gh_org = os.environ.get("GH_ORG", None)

    if gh_hostname is None:
        print("Environment varible [bold]GH_HOSTNAME[/bold] must be set")
        print("$ export [bold]GH_HOSTNAME=<github.com>[/bold]")
        raise ValueError("Invalid value")
    if gh_org is None:
        print("Environment varible [bold]GH_ORG[/bold] must be set")
        print("$ export [bold]GH_ORG=<my-organization>[/bold]")
        raise ValueError("Invalid value")

    # Get secret from user
    print("\n" + "-" * 50)
    print(f"GH_HOSTNAME={gh_hostname}")
    print(f"GH_ORG={gh_org}")
    gh_personal_token = typer.prompt("What's your Github Personal token?")
    print("-" * 50)

    return gh_hostname, gh_org, gh_personal_token
