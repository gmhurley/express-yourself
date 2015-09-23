import re


def words(inp):
    return re.findall(r'(\b[a-z0-9]*[a-z\-]\b)', inp, re.IGNORECASE)
