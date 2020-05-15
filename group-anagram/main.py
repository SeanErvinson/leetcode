def test(anagrams):
    groups = {}
    for s in anagrams:
        groups.setdefault(tuple(sorted(s)), []).append(s)
    return groups.values()

# def test(anagrams):
#     groups = {}
#     for word in anagrams:
#         words = tuple(sorted(word))
#         if words not in groups:
#             a = []
#             a.append(word)
#             groups[words] = a
#         else:
#             groups[words].append(word)
#     return list(groups.values())

print(test(["eat", "tea", "tan", "ate", "nat", "bat"]))
print(test(["cab", "tin", "pew", "duh", "may", "ill", "buy", "bar", "max", "doc"]))
print(
    test(
        [
            "hos",
            "boo",
            "nay",
            "deb",
            "wow",
            "bop",
            "bob",
            "brr",
            "hey",
            "rye",
            "eve",
            "elf",
            "pup",
            "bum",
            "iva",
            "lyx",
            "yap",
            "ugh",
            "hem",
            "rod",
            "aha",
            "nam",
            "gap",
            "yea",
            "doc",
            "pen",
            "job",
            "dis",
            "max",
            "oho",
            "jed",
            "lye",
            "ram",
            "pup",
            "qua",
            "ugh",
            "mir",
            "nap",
            "deb",
            "hog",
            "let",
            "gym",
            "bye",
            "lon",
            "aft",
            "eel",
            "sol",
            "jab",
        ]
    )
)
