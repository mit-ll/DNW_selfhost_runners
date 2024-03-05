<p align="center">
  <a href="https://github.com/destin-v">
    <img src="https://drive.google.com/uc?export=view&id=1yFte-RASCcF1ahkYg1Jybavi-gWje8kp" alt="drawing" width="500"/>
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
  <a href="https://github.com/destin-v/vs_codex/actions/workflows/pre-commit.yml">  <img alt="pre-commit" src="https://github.com/destin-v/vs_codex/actions/workflows/pre-commit.yml/badge.svg"></a>
  <a href="https://destin-v.github.io/vs_codex/src.html">                           <img alt="pdoc" src="https://github.com/destin-v/vs_codex/actions/workflows/pdoc.yml/badge.svg"></a>
  <a href="https://github.com/destin-v/vs_codex/actions/workflows/pytest.yml">      <img alt="pytest" src="https://github.com/destin-v/vs_codex/actions/workflows/pytest.yml/badge.svg"></a>
</p>

# 📒 Description
Github Actions is an event based scheduler that triggers based on user defined events.  A commmon use for Github Actions is Continuous Integration / Continuous Development (CI/CD).  But Github Actions can be configured to trigger off of any user defined event.  This makes them very powerful for scheduling jobs.

## Create Github Token
In order to use Github runners you first need to create an ***organization***.  An organization allows you add members and projects.  Git runners assigned to an organization and will automatically process jobs that belong to that organization.

In order to create a Git runner you need to create a classic **Github token** via:

* Settings > Developer Settings > Personal Access Tokens > Tokens (classic)

A Github personal token is an identifier that lets Github Actions know who you are.  Think of it as a userId.  Make sure you allow all permissions.

To make your Github personal token available to your API calls it is best to set it in the environment:

```bash
export GITHUB_TOKEN=<GITHUB_TOKEN>
```

To pass an environment variable into an Apptainer/Singularity container:

```bash
singularity run --env GITHUB_TOKEN=$GITHUB_TOKEN <container.sif>
```

## Git Runner Code
You must download the code for a Git runner [**here**](https://github.com/actions/runner/releases).  Note the version number because self-hosting may require versions within a certain range.  Once you have identified the version you want, copy the download code into your container.

## Git Runner Commands
Rest API commands can be found [**here**](https://docs.github.com/en/rest/actions/self-hosted-runners?apiVersion=2022-11-28).  Pay special attention to the `hostname` and the `token` type.  These often cause confusion because the URL changes based on the type of command requested.  For standardized API calls consider using the [**gh cli**](https://cli.github.com/).

# Container Deployment

To create a container with Git runner:

```bash
cd containers
singularity build base.sif base.def
singularity build runner.sif runner.def
```

To host a Git runner simply run the container via:

```bash
singularity run --userns --writable --env GITHUB_TOKEN=$GITHUB_TOKEN runner.sif
```
