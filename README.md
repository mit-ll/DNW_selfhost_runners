# Git Actions
Github Actions is an event based scheduler that triggers based on user defined events.  A commmon use for Github Actions is Continuous Integration / Continuous Development (CI/CD).  But Github Actions can be configured to trigger off of any user defined event.  This makes them very powerful for scheduling jobs.

## Create Github Token
In order to use Github runners you first need to create an *organization*.  An organization allows you to group members and projects together.  Git runners are assigned to an organization and will process jobs from an organization.

In order to create a Git runner you need to create a classic Github token via: 

* Settings > Developer Settings > Personal Access Tokens > Tokens (classic)

Make sure you assign allow all permissions.

## Common Commands
### List Runners (LLCAD Dev)

```bash
github_runners = curl -L \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <GITHUB TOKEN>" \
  -H "X-GitHub-Api-Version: 2022-11-28" \
  https://api.llcad-github-dev.llan.ll.mit.edu/orgs/git-runners/actions/runners
```

### Create registration token
```bash
registration = curl -L \
  -X POST \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <GITHUB TOKEN>" \
  -H "X-GitHub-Api-Version: 2022-11-28" \
  https://api.llcad-github-dev.llan.ll.mit.edu/orgs/git-runners/actions/runners/registration-token
```

### Create JIT runner
```bash
curl -L \
  -X POST \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <GITHUB TOKEN>" \
  -H "X-GitHub-Api-Version: 2022-11-28" \
  https://llcad-github-dev.llan.ll.mit.edu/api/v3/orgs/git-runners/actions/runners/generate-jitconfig \
  -d '{"name":"New runner","runner_group_id":1,"labels":["self-hosted","X86","ubuntu-latest"],"work_folder":"_work"}'
```

