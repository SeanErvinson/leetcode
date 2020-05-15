def test(s):
    duplicates = []
    sub_palindrome = 0
    sub_palindrome += len(set(s))
    for i in range(len(s)):
        for j in range(len(s)):
            print(s[:i+1],  s[j::-1])
            if s[:i+1] == s[j::-1] and s[:i+1] not in duplicates:
                duplicates.append(s[:i+1])
                sub_palindrome+=1

    print(duplicates)

print(test("aabaa"))