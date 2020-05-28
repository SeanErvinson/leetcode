def test(str):
    result = ""
    for char in str:
        decimal = ord(char)
        if 65 <= decimal and decimal <= 90:
            result += chr(decimal + 32)
        else:
            result += char
    return result


print(test("Hello"))
print(test("here"))
print(test("LOVELY"))
print(test("1231"))
print(test("&#!@"))
print(test("AS3hAd9$#"))
