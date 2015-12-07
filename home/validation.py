import re

EMAIL_REGEX = re.compile(r'[^@]+@[^@]+\.[^@]+')

def not_numberic(n):
    try:
        float(n)
        return False
    except ValueError:
        return True

def validate(email, amount):
    if not EMAIL_REGEX.match(email) or not_numberic(amount):
        return False
    return True