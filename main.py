import asyncio
from function.online import set_all_online
from function.joiner import joinah
from function.spammer import spammer

async def main():
    status_text = input("Enter status text (default: Hello, World!) [>] ") or "Hello, World"
    presence = input("Enter presence (Online, Idle, Busy, Focus) (default: Online) [>] ") or "Online"

    await set_all_online(status_text, presence)

    choice = input("1) Joiner\n2) Spammer\nSelect Choice [>] ")

    if choice == '1':
        inviteCode = input('Invite CODE [!] > ')
        await joinah(inviteCode)
    elif choice == '2':
        msg = input("Message to spam? [>] ")
        count = int(input("How many times to send? [>] "))
        await spammer(msg, count)

if __name__ == '__main__':
    asyncio.run(main())
