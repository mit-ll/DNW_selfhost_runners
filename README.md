<p align="center">
  <a href="https://github.com/destin-v">
    <img src="https://raw.githubusercontent.com/destin-v/destin-v/main/docs/pics/logo.gif" alt="drawing" width="500"/>
  </a>
</p>

# 📒 Description
<p align="center">
  <img src="docs/pics/program_logo.png" alt="drawing" width="350"/>
</p>

<p align="center">
  <a href="https://devguide.python.org/versions/">              <img alt="" src="https://img.shields.io/badge/python-^3.10-blue?logo=python&logoColor=white"></a>
  <a href="https://docs.github.com/en/actions/quickstart">      <img alt="" src="https://img.shields.io/badge/CI-github-blue?logo=github&logoColor=white"></a>
  <a href="https://black.readthedocs.io/en/stable/index.html">  <img alt="" src="https://img.shields.io/badge/code%20style-black-blue"></a>
</p>

<p align="center">
  <a href="https://github.com/mit-ll/github-selfhosted-runners/actions/workflows/pre-commit.yml">  <img alt="pre-commit" src="https://github.com/mit-ll/github-selfhosted-runners/actions/workflows/pre-commit.yml/badge.svg"></a>
  <a href="https://github.com/mit-ll/github-selfhosted-runners/actions/workflows/pytest.yml">      <img alt="pytest"     src="https://github.com/mit-ll/github-selfhosted-runners/actions/workflows/pytest.yml/badge.svg"></a>
</p>

# 📒 Description
Github Actions is an event based scheduler that triggers based on user defined events.  A commmon use for Github Actions is Continuous Integration / Continuous Development (CI/CD).  But Github Actions can be configured to trigger off of any user defined event.  This makes them very powerful for scheduling jobs.

## Requirements
In order to use Github Self-hosted Runners (GSR) you need three things:
* **Github Hostname**:
  * https://**github-hostname**.com
* **Github Organization**
  * https://**github-hostname**/settings/**organizations**
* **Github Personal Access Token**
  * Settings > Developer Settings > Personal Access Tokens > Tokens (classic)

> [!NOTE]
> A Github personal token is an identifier that lets Github Actions know who you are.  Think of it as a userId.  Make sure you allow all permissions.

## Git Runner Code
You must download the code for a Git runner [**here**](https://github.com/actions/runner/releases).  Note the version number because self-hosting may require versions within a certain range.  Once you have identified the version you want, copy the download code into your container.

## Git Runner Commands
Rest API commands can be found [**here**](https://docs.github.com/en/rest/actions/self-hosted-runners?apiVersion=2022-11-28).

Pay special attention to the `hostname` and the `token` type.  For standardized API calls see the [**Github CLI**](https://cli.github.com/).

# 🐳 Container Deployment

## Building Container

You must configure the `gh.config` and `gh.secret` files prior to building.  The `gh.config` point toward your hostname and organization while the `gh.secret` is simply your Github Personal Access token.

```bash
# gh.config
export GH_HOSTNAME=<hostname>
export GH_ORG=<Github organization>
```

```bash
# gh.secret
ghp_XXXXXXXXXXXXXXXXXXXXXXXXX
```

Perform a build with the following commands:

```bash
cd containers
singularity build base.sif base.def
singularity build runner.sif runner.def
```

Finally run a test to verify that the runner is successful.

```bash
singularity run \
  --userns \
  --writable \
  --app test \
  runner.sif
```

## Deploying Instances
If you need multiple Git runners operating on the system try using instances:

```bash
singularity instance start --userns --tmp-sandbox --writable runner.sif runner1
singularity instance start --userns --tmp-sandbox --writable runner.sif runner2

# Start runners
singularity run --app start_runner instance://runner1
singularity run --app start_runner instance://runner2

# List runners
singularity instance list

# Shell into runner
singularity shell instance://runner1

# Stop all runners
singularity run --app stop_runner instance://runner1
singularity run --app stop_runner instance://runner2
```
