import os

from dotenv import load_dotenv

load_dotenv()


def call_anthropic():
    from anthropic import Anthropic

    client = Anthropic(api_key=os.environ["ANTHROPIC_API_KEY"])
    msg = client.messages.create(
        model="claude-sonnet-4-5",
        max_tokens=100,
        messages=[{"role": "user", "content": "Say hello in one short sentence."}],
    )
    print("Anthropic response:", msg.content[0].text)


def call_openai():
    from openai import OpenAI

    client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])
    resp = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": "Say hello in one short sentence."}],
        max_tokens=100,
    )
    print("OpenAI response:", resp.choices[0].message.content)


if __name__ == "__main__":
    call_anthropic()
    call_openai()
