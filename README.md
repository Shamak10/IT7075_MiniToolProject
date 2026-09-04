# IT7075 Mini Project: AI Tools and Environment Setup

Environment configuration project for IT7075 — local dev setup, version control,
hosted notebooks, managed LLM credentials, cloud VM, and an isolated virtualization lab.

## Setup

```bash
python3.12 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env   # then fill in real keys, never commit this file
```

Select `.venv` as the VS Code interpreter and Jupyter kernel (bottom-right status bar,
or Cmd+Shift+P -> "Python: Select Interpreter").

## Files

- `hello.py` — interpreter sanity-check script.
- `resource_inventory.py` — local hardware/GPU inventory (system_profiler + torch).
- `llm_test.py` — local script calling Anthropic (Claude) using `.env` credentials.
- `local_test.ipynb` — notebook run inside VS Code against the `.venv` kernel.
- `colab_notebook.ipynb` — uploaded to Google Colab for Drive persistence and
  Colab Secrets-based model access.

## LLM provider

Anthropic (Claude) is used for §3.5. `openai` was dropped from the project
after the OpenAI trial credit was exhausted with no further funding — the
assignment only requires one approved provider.

## Security

`.env` and `.venv/` are excluded via `.gitignore`. Credentials are loaded from
environment variables (`.env` locally, Colab Secrets in the hosted notebook) and
never appear in source or committed files.
