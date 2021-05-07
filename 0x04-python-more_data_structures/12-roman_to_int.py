#!/usr/bin/python3
def roman_to_int(roman_string):
    if (
        roman_string is None
        or not roman_string
        or not isinstance(roman_string, str)
    ):
        return 0
    val = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    for k in roman_string:
            if k not in val.keys():
                return 0

    # Inicialize character
    p = 0
    ans = 0
    # traverse all characters
    n = len(roman_string)

    for i in range(n-1, -1, -1):
        # if greater of list val
        if val[roman_string[i]] >= p:
            ans += val[roman_string[i]]
        # if smaller
        else:
            ans -= val[roman_string[i]]
        # update previous
        p = val[roman_string[i]]
    return ans
