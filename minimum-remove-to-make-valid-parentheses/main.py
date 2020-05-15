def test(s):
    stack_brackets = []
    open_bracket = 0
    result = []
    for char in s:
        if char == "(":
            open_bracket += 1
        elif char == ")":
            if open_bracket == 0:
                continue
            open_bracket -= 1
        result.append(char)
    for i in reversed(range(len(result))):
        if result[i] == "(" and open_bracket != 0:
            result.pop(i)
            open_bracket -= 1
    return "".join(result)


# print(test("())()((("))
print(test("))(("))
