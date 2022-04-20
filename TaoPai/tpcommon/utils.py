# coding: utf-8

FLAG = "TokenID:"

def get_tokenid_from_html_text(text):
    flag_pos = text.find(FLAG)
    if flag_pos != -1:
        items = text[flag_pos+len(FLAG):].strip().split()
        token_id = int(items[0])
        return token_id