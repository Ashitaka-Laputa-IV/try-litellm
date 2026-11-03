"""Minimal LangChain + OpenCode Go smoke test."""

from dotenv import load_dotenv
from langchain.chat_models import init_chat_model


def main() -> None:
    load_dotenv()

    llm = init_chat_model(
        "litellm:opencode_go/deepseek-v4.1-flash",
        model_kwargs={"litellm_session_id": "try-litellm"},
    )
    print(f"\n{type(llm).__name__}: {llm.model}")
    print(llm.invoke("Reply with exactly: OpenCode Go is working.").content)

if __name__ == "__main__":
    main()
