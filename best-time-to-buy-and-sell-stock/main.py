def test(days_price):
    total_profit = 0
    if len(days_price) == 0 and not days_price:
        return 0
    for i in range(0, len(days_price) - 1):
        if days_price[i + 1] > days_price[i]:
            total_profit += days_price[i + 1] - days_price[i]
    return total_profit


# test([7,1,5,3,6,4])
test([1,2,3,4,5])
