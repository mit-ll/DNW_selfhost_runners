# 🤖 Git Actions
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
## Common Commands
Most of the common API commands can be found [**here**](https://docs.github.com/en/rest/actions/self-hosted-runners?apiVersion=2022-11-28).

### List Runners

```bash
curl -L \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer ${GITHUB_TOKEN}" \
  -H "X-GitHub-Api-Version: 2022-11-28" \
  https://api.llcad-github-dev.llan.ll.mit.edu/orgs/git-runners/actions/runners
```

### Create Github Runner Token
Runner tokens are needed whenever you want to create a new runner.  These API calls need a Github personal access token in order to generate a runner token.

To view on the command line:
```bash
curl -L \
  -X POST \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer ${GITHUB_TOKEN}" \
  -H "X-GitHub-Api-Version: 2022-11-28" \
  https://api.llcad-github-dev.llan.ll.mit.edu/orgs/git-runners/actions/runners/registration-token
```

To save as environment variable:
```bash
RUNNER_TOKEN=$(curl    -s \
                -L \
                -X POST \
                -H "Authorization: Bearer ${GITHUB_TOKEN}" \
                -H "Accept: application/vnd.github+json" -H "X-GitHub-Api-Version: 2022-11-28" \
                --url "https://api.llcad-github-dev.llan.ll.mit.edu/orgs/git-runners/actions/runners/registration-token" \
                | jq .token --raw-output)
```

### Create JIT Runner
Create  a JIT runner.

```bash
curl -L \
  -X POST \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer ${GITHUB_TOKEN}" \
  -H "X-GitHub-Api-Version: 2022-11-28" \
  https://llcad-github-dev.llan.ll.mit.edu/api/v3/orgs/git-runners/actions/runners/generate-jitconfig \
  -d '{"name":"New runner","runner_group_id":1,"labels":["self-hosted","X64","ubuntu-latest"],"work_folder":"_work"}'
```