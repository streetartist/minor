import re

def run(string: str) -> str:
    if re.match(r'\s+print,\s+', string):
        pass
    return