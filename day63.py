# 11 - May - 2020

# Decode String

# Given a string with a certain rule: k[string] should be expanded to string k times.
# So for example, 3[abc] should be expanded to abcabcabc. Nested expansions can happen,
# so 2[a2[b]c] should be expanded to abbcabbc.

def decodeString(s):
    # Fill this in.
    if is_integer(s[0]):
        return int(s[0]) * decodeString(s[1:])
    else:
        if s[0] == '[':
            end = s.rindex(']')
            if end + 1 < len(s):
                return decodeString(s[1:end]) + s[end+1:]
            else:
                return decodeString(s[1:end])
        elif s.find('[') > 0:
            end = s.rindex(']')
            if end + 1 < len(s):
                return s[0] + decodeString(s[1:end+1]) + s[end+1:]
            else:
                return s[0] + decodeString(s[1:end+1])
        else:
            return s




def is_integer(n):
    try:
        float(n)
    except ValueError:
        return False
    else:
        return float(n).is_integer()


print(decodeString('2[a2[b]c]'))
# abbcabbc