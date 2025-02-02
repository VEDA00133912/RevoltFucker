import aiohttp
import asyncio
import json

async def send_message(session, channelid, msg, token):
    headers = {
        'authority': 'api.revolt.chat',
        'origin': 'https://app.revolt.chat',
        'referer': 'https://app.revolt.chat/',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.82 Safari/537.3',
        'x-session-token': token
    }

    async with session.post(f'https://api.revolt.chat/channels/{channelid}/messages', headers=headers, json={'content': msg}) as res:
        response_text = await res.text()
        if res.status == 200:
            print(f"[SPAMMER] Sent message in {channelid} on token ---> {token[:10]}...")
        else:
            print(f"[SPAMMER] Failed to send message in {channelid} on token ---> {token[:10]}...")

async def spammer(msg, count):
    async with aiohttp.ClientSession() as session:
        with open("data/tokens.txt") as f:
            tokens = f.read().splitlines()
        with open("data/channels.txt") as f:
            channels = f.read().splitlines()

        for i in range(count):
            tasks = [send_message(session, channel, msg, token) for channel in channels for token in tokens]
            await asyncio.gather(*tasks)
