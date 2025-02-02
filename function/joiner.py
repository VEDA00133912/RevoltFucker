import aiohttp

async def joinah(inviteCode):
    async with aiohttp.ClientSession() as session:
        with open("data/tokens.txt") as f:
            tokens = f.read().splitlines()
        
        for token in tokens:
            headers = {
                'authority': 'api.revolt.chat',
                'origin': 'https://app.revolt.chat',
                'referer': 'https://app.revolt.chat/',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.82 Safari/537.3',
                'x-session-token': token
            }
            async with session.post(f'https://api.revolt.chat/invites/{inviteCode}', headers=headers, json={}) as res:
                print(f"[JOINER] {'Joined' if res.status == 200 else 'Failed'} Server on token ---> {token}")
