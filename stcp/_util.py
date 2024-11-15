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

def get_real_time_url(stop_code, hash_code, meta_hash_key='hash123', meta_filename='soapclient'):
    return f'https://www.stcp.pt/pt/itinerarium/{meta_filename}.php?codigo={stop_code}&linha=0&{meta_hash_key}={hash_code}'
