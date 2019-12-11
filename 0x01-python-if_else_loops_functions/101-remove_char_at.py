#!/usr/bin/python3
def remove_char_at(str, n):
    new_str = format(str[:n] + str[n+1:] if n >= 0 else str)
    return (new_str)
