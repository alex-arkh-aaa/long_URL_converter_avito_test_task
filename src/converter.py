import string
from secrets import choice


ALPHABET: str = string.ascii_letters + string.digits

def generate_url() -> str:
    slug = ''
    for symbol in range(6):
        slug += choice(ALPHABET)
    return slug
