import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY"),
)

def ask_jarvis(prompt: str) -> str:
    response = client.chat.completions.create(
        model="google/gemma-4-26b-a4b-it:free",
        messages=[
            {
                "role": "system",
                "content": "تو یک دستیار هوشمند شخصی به اسم جارویس هستی. کوتاه، مفید و به فارسی جواب بده."
            },
            {"role": "user", "content": prompt}
        ],
        max_tokens=1200,
        temperature=0.4,
    )
    return response.choices[0].message.content

if __name__ == "__main__":
    prompt = os.getenv("PROMPT", "سلام جارویس، وضعیت امروز چطوره؟ یک گزارش کوتاه بده.")
    print("جارویس در حال فکر کردن...")
    answer = ask_jarvis(prompt)
    print("\n===== پاسخ جارویس =====\n")
    print(answer)
