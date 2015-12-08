import re
from django.db.models import Max

EMAIL_REGEX = re.compile(r'[^@]+@[^@]+\.[^@]+')

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
            return 0 #valid
        return 1 #bid not high enough
    return -1 #invalid entry
