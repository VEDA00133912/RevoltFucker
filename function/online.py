import aiohttp
import json
import asyncio
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))  
TOKENS_FILE = os.path.join(BASE_DIR, "..", "data", "tokens.txt")

async def set_online(token, status_text, presence):
    headers = {
        "Content-Type": "application/json",
        "x-session-token": token.strip()
    }
    payload = {
        "status": {"text": status_text, "presence": presence},
        "online": True
    }

    async with aiohttp.ClientSession() as session:
        async with session.patch("https://app.revolt.chat/api/users/@me", headers=headers, data=json.dumps(payload)) as response:
            return await response.text()

async def set_all_online(status_text, presence):
    if not os.path.exists(TOKENS_FILE):
        print(f"Error: Token file not found: {TOKENS_FILE}")
        return

    with open(TOKENS_FILE, "r") as f:
        tokens = [line.strip() for line in f if line.strip()]

    if not tokens:
        print("Error: No tokens found in tokens.txt")
        return

    await asyncio.gather(*(set_online(token, status_text, presence) for token in tokens))
