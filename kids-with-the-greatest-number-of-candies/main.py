def test(candies, extraCandies):
    highest_candy = max(candies)
    result = []
    for candy in candies:
        result.append(candy+extraCandies >= highest_candy)
    return result
    # return list(map(lambda candy: candy + extraCandies >= max(candies), candies))


print(test([12, 1, 12], 10))
print(test([4, 2, 1, 1, 2], 1))
print(test([2, 3, 5, 1, 3], 3))

