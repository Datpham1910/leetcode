def reverse_vowels(s: str) -> str:
    vowels = 'ueoaiUEOAI'
    i, j = 0, len(s) - 1
    str_list = list(s)

    while i < j:
        if s[i] not in vowels:
            i += 1
        elif s[j] not in vowels:
            j -= 1
        else:
            str_list[i], str_list[j] = str_list[j], str_list[i]
            i += 1
            j -= 1

    return "".join(str_list)

print(reverse_vowels('hello'))