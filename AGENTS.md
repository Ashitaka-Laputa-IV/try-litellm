# AGENTS.md

## Project

Small Python 3.14 project managed by `uv`. It is a minimal LangChain + `langchain-litellm` smoke test against OpenCode Go.

- Entry point: `src/try_litellm/main.py:main`, exported from `src/try_litellm/__init__.py`.
- The model is created with `init_chat_model("litellm:opencode_go/deepseek-v4.1-flash")`.
- Dependencies are declared in `pyproject.toml`; `uv.lock` is authoritative.
- `litellm[mcp]==1.109.0.dev2` is pinned because it is the first published version with the `opencode_go` provider. Do not downgrade to `1.106.6` or use the compromised `1.107.0`.
- Use `uv add` / `uv sync`; do not use plain `pip install` against this environment.

## Commands

```bash
uv sync
uv run try-litellm
```

There is no lint, typecheck, or test suite configured yet.

## OpenCode Go integration

The code uses LiteLLM's native provider:

```python
init_chat_model(
    "litellm:opencode_go/deepseek-v4.1-flash",
    model_kwargs={"litellm_session_id": "try-litellm"},
)
```

- Auth: `OPENCODE_API_KEY`.
- Session: `model_kwargs={"litellm_session_id": "..."}` is forwarded as `x-opencode-session`.
- Keep the native `opencode_go/` provider. Do not add an `openai/` + `api_base` fallback.
- Stable release tracking: https://github.com/BerriAI/litellm/issues/49829

## Secrets

- `.env` is gitignored and holds the real `OPENCODE_API_KEY`; never print or commit it.
- `.env.example` is tracked and must stay secret-free.

## Git

- Default branch: `main`.
- `.gitattributes` enforces `* text=auto` (LF normalization).
