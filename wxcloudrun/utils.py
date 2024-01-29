def trunc_open_id(open_id):
    if len(open_id) == 28:
        return open_id
    if len(open_id) > 28:
        return open_id[-28:]
    if len(open_id) < 28:
        return "0" * (28 - len(open_id)) + open_id