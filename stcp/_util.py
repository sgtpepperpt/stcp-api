def get_internal_line_code(line_code: str):
    """
    Converts the human-readable line code into the internal one (e.g. ZC -> 107)
    :param line_code: the human-readable line code
    :return: the internal line code
    """
    from stcp._primitives import get_lines

    for line in get_lines():
        if line['pubcode'] == line_code:
            return line['code']

    raise Exception('Invalid line code')
