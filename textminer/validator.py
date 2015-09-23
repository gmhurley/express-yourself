import re

# assert v.binary("0")
# assert v.binary("1")
# assert v.binary("01")
# assert v.binary("10")
# assert v.binary("1110100010")
# assert not v.binary("")
# assert not v.binary("911")


def binary(inp):
    match = re.search(r'([0-1]+)', inp)
    # if not inp is testing if string is empty
    if not inp or inp != match.groups()[0]:
        return False
    return True


def binary_even(inp):
    if not binary(inp) or int(inp) % 2 != 0:
        return False
    return True


def hex(inp):
    try:
        int(inp, 16)
        return True
    except:
        return False


def word(inp):
    if not inp:
        return False
    match = re.findall(r'(\b[a-z0-9]*[a-z\-]\b)', inp, re.IGNORECASE)
    joined = ' '.join(match)
    if '- ' in joined:
        joined = joined.replace('- ', '-')
    if match is None or inp != joined:
        return False
    return True


def words(inp, count=0):
    if count == 0:
        return word(inp)
    match = re.findall(r'(\b[a-z0-9]*[a-z\-]\b)', inp, re.IGNORECASE)
    joined = ' '.join(match)
    if '- ' in joined:
        joined = joined.replace('- ', '-')
    if len(list(joined.split())) == count:
        return True
    return False


def phone_number(inp):
    match = re.search(r'(\(?[0-9]{3}\)?[-. ]?[0-9]{3}[-. ]?[0-9]{4})', inp)
    if match is None or match.groups()[0] != inp:
        return False
    return True


def money(inp):
    return re.match(r'\$([0-9]+(,[0-9]{3})*)(\.[0-9]{2})?$', inp)


def zipcode(inp):
    return re.match(r'[0-9]{5}(-[0-9]{4})?$', inp)


def date(inp):
    return re.match(r'\d+[\/-]+\d+[\/-]\d*', inp)
