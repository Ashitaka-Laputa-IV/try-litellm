# try-litellm

Minimal LangChain + `langchain-litellm` + OpenCode Go smoke test.

```bash
cp .env.example .env   # then set OPENCODE_API_KEY
uv sync
uv run try-litellm
```

It creates and calls the native LiteLLM provider:

```python
init_chat_model(
    "litellm:opencode_go/deepseek-v4.1-flash",
    model_kwargs={"litellm_session_id": "try-litellm"},
)
```

`litellm==1.109.0.dev2` is pinned because it is the first published version with the `opencode_go` provider. Switch back to a stable LiteLLM release once one includes it: https://github.com/BerriAI/litellm/issues/49829
