def jewels_and_stones(jewels, stones):
    sum = 0
    for stone in stones:
        if stone in jewels:
            sum+=1
    return sum

def jewels_and_stones_one_liner_map(jewels, stones):
    return sum(map(jewels.count, stones))

def jewels_and_stones_one_liner(J, S):
    return sum(s in J for s in S)

print(jewels_and_stones("aA", "aAAbbbb"))
print(jewels_and_stones_one_liner("aA", "aAAbbbb"))
print(jewels_and_stones_one_liner("aA", "aAAbbbb"))