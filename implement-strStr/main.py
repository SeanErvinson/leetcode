def test(haystack, needle):
    if not needle:
        return 0
    pointer = 0
    result = -1
    if len(needle) > len(haystack):
        return result
    for index, char in enumerate(haystack):
        if char != needle[pointer]:
            continue
        if result == -1:
            result = index
        pointer += 1
        if pointer >= len(needle):
            return result
        if haystack[index + 1] != needle[pointer]:
            result = -1
            pointer = 0
    return result

    # return haystack.find(needle)


print(test("mississippi", "issip"))  # 4
print(test("aaa", "aaaa"))  # -1
print(test("dfjlaourq", "dflao"))  # -1
print(test("dflaourq", "o"))  # 4
print(test("hello", "eo"))  # -1
print(test("sean", "an"))  # 2
print(test("aaa", "a"))  # 0
print(test("hello", "ll"))  # 2
print(test("hefslkdfjlaourq", "dfjlao"))  # 6
print(test("aaaaaa", "bba"))  # -1
