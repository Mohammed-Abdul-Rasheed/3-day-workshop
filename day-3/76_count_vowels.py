def count_vowels(text):
    if text=="":
        return 0
    return (1 if text[0].lower() in "aeiou" else 0)+count_vowels(text[1:])

print(count_vowels(input()))
