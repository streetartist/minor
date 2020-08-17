import re

from .AST import string as AST_string

def run(string: str) -> str:
    print_re = re.compile(r'''^\s*print\s*,\s*(.*?)\s*$''')
    result = print_re.findall(string)
    if result:
        return AST_string(result[0], 0)[0]
    return "Error"