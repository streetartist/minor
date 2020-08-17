import re

def run(string: str) -> str:
    print_re = re.compile(r'''^\s*print\s*,\s*(["'])(.*?)\1\s*$''')
    result = print_re.findall(string)
    if result:
        return result[0][1]
    return "Error"