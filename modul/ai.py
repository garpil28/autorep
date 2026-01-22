import requests
from config import OPENAI_API_KEY

async def ai_generate(prompt):
    try:
        if OPENAI_API_KEY:
            r = requests.post(
                "https://api.openai.com/v1/chat/completions",
                headers={"Authorization": f"Bearer {OPENAI_API_KEY}"},
                json={
                    "model": "gpt-3.5-turbo",
                    "messages": [{"role": "user", "content": prompt}],
                    "max_tokens": 200
                }
            )
            return r.json()["choices"][0]["message"]["content"]

        r = requests.post("https://api-free.akira.ai/generate", json={"prompt": prompt})
        return r.text

    except:
        return "⚠️ AI sedang error."
