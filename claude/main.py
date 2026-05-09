from .client.llm_client import LLMClient
import asyncio
import click

class CLI:
    def __init__(self):
        pass

    def run_single():


async def run(messages: dict[str, Any]):
    client = LLMClient()

    async for event in client.chat_completion(messages, True):
        print(event)


@click.command()
@click.argument("prompt", required=False)
def main(
    prompt: str | None,
):
    print(f"User prompt: {prompt}")
    messages = [{"role": "user", "content": prompt or "Hello"}]
    asyncio.run(run(messages))

if __name__ == "__main__":
    main()