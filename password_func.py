import hashlib
import logging
from random import choice, randint, shuffle
from string import digits, ascii_lowercase, ascii_uppercase, ascii_letters


def is_hashlike(string: str):
    ' check if string is all hex and likely a hashed pasword'
    try:
        int(string, 16)
        return True
    except ValueError:
        return False


def hash_password(password):
    if is_hashlike(password):  # don't rehash likely hashed password
        return password
    hashed = hashlib.sha256(password.encode())
    logging.info(f"\n\thashed {password}\n\tto     {hashed.hexdigest()}")
    return hashed.hexdigest()

def check_password(plain_password, employee_password):
    hashed_password = hash_password(plain_password)
    return hashed_password == employee_password


def password_bad(password):
    return password in BAD_PASSWORDS or (is_hashlike(password) and password in BAD_HASHED_PASSWORDS)


def generate_password(size=16):
    limit = min(3, max(1, size//5))
    specials = [choice(PUNCTUTATION) for _ in range(randint(1, limit))]
    nums = [choice(digits) for _ in range(randint(1, 4))]
    lowers = [choice(ascii_lowercase) for _ in range(randint(1, limit))]
    uppers = [choice(ascii_uppercase) for _ in range(randint(1, limit))]
    password = specials + nums + lowers + uppers
    shuffle(password)
    password = [choice(ascii_letters)] + password
    if len(password) >= size:
        password = password[:size]
    else:
        password.extend([choice(ascii_letters) for _ in range(size - len(password))])
    logging.info(f'\n\tpassword generated: {"".join(password)}')
    return ''.join(password[:size])



logging.basicConfig(filename='password_func.log', filemode='a',
                    format='%(asctime)s - %(message)s',
                    level=logging.INFO)

logging.info('imported/run')

DEFAULT_PASSWORD = 'password'
BAD_PASSWORDS = (DEFAULT_PASSWORD, "", 'Password', 'Passw0rd',
                 'password1', 'passw0rd1', 'Passw0rd1')
BAD_HASHED_PASSWORDS = [hash_password(p) for p in BAD_PASSWORDS]
PUNCTUTATION = r'!#$%&\()*+-/:;<=>?@[\\]^_`{|}~'
