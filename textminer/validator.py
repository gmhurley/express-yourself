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
