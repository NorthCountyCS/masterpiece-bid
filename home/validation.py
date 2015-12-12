from django.db.models import Max
import re

EMAIL_REGEX = re.compile(r'[^@]+@[^@]+\.[^@]+')
INVALID = 0
VALID = 1
LOW_BID = 2

def is_numberic(n):
    try:
        float(n)
        return True
    except ValueError:
        return False

def validate(name, email, amount, art):
    max_bid = art.bid_set.all().aggregate(Max('amount'))['amount__max']
    valid_len = len(amount.split('.')[0]) <= 4
    if len(name) > 0 and EMAIL_REGEX.match(email) and (max_bid == None or is_numberic(amount)) and valid_len:
        if max_bid == None or float(amount)-float(max_bid) >= 1:
            return VALID
        return LOW_BID
    return INVALID
