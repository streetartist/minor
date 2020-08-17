
def string(string: str, index: int) -> (str, int):
    """
    It will get a string and the begin index, and return the string value and
    the end index.
    """
    state = {
        'quota': None
    }
    if string[index] == "'":
        state['quota'] = "'"
    elif string[index] == '"':
        state['quota'] = '"'
    else:
        # TODO: fix there to return a Error value.
        return "Error", index + 1

    result = ''
    while True:
        # looking for the next character
        index += 1
        # if need escape
        if string[index] == '\\':
            index += 1
            if string[index] == '\\':
                result += '\\'
            elif string[index] == '"':
                result += '"'
            elif string[index] == "'":
                result += "'"
            else:
                result += string[index]
        # else if it touch the end place
        elif string[index] == state['quota']:
            break
        # else it touch the normal character
        else:
            result += string[index]

    return result, index + 1
