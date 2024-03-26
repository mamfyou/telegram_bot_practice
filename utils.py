from telethon import TelegramClient


def telegram_client():
    api_id = 6669515164
    api_hash = 'AAFjmRvlzRhIfeNXgOudrJK_beelhClJjeQ'
    session_name = 'mamf'
    client = TelegramClient(session_name, api_id, api_hash)
    return client
