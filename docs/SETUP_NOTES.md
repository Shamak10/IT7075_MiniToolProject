# Configuration notes

## Local environment
- Python 3.12 (Homebrew `python@3.12`) used for the venv instead of the macOS
  system Python 3.9, for current package/wheel compatibility (e.g. torch).
- venv created with `python3.12 -m venv .venv`; selected as both the VS Code
  interpreter and the Jupyter kernel via `.vscode/settings.json`
  (`python.defaultInterpreterPath`).
- VS Code extensions installed: `ms-python.python`, `ms-toolsai.jupyter`,
  `github.vscode-pull-request-github`.

## Credentials
- API keys are loaded from `.env` locally (via `python-dotenv`) and from
  Colab Secrets in the hosted notebook — never hardcoded, never committed.
  `.env` and `.venv/` are excluded in `.gitignore`.

## Virtualization (§3.7)
- Host is Apple Silicon (arm64). Metasploitable2 requires a 32-bit x86 guest,
  which VirtualBox/VMware cannot run on Apple Silicon, so the assignment's
  documented alternative was used instead: a containerized target
  (OWASP Juice Shop) run under Docker Desktop.
- Network mode: Docker's default bridge network with a published port
  (`-p 3000:3000`), which is the functional equivalent of NAT — the container
  gets a private address on an isolated virtual subnet (172.17.0.0/16) and is
  reached from the host only through the explicitly published port.
- Note: on Docker Desktop for Mac, containers run inside a hidden Linux VM, so
  ICMP ping from the host to a container's internal bridge IP does not
  resolve (times out) even though the service is reachable over its published
  port. Reachability was verified with `curl http://localhost:3000` (HTTP 200)
  instead of ICMP ping, which is the correct/expected verification method for
  this network architecture.

## Jetstream2
- SSH keypair generated locally ahead of VM creation
  (`~/.ssh/jetstream2` / `~/.ssh/jetstream2.pub`, ed25519) so the public key
  can be pasted into the Jetstream2 dashboard or added via `cloud-init`/
  `ssh-import-id` at instance launch.
