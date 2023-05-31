import string
from random import choice

from config import get_settings

alphanum = list(string.ascii_lowercase + string.digits)
key_lenght = get_settings().KEY_LENGTH


def shorten_url() -> str:
    key = "".join([choice(alphanum) for _ in range(key_lenght)])
    return key
