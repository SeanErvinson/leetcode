def sortArrayByParity(numbers):
    sorted_parity = []
    [
        sorted_parity.insert(0, number)
        if not number % 2
        else sorted_parity.insert(len(sorted_parity), number)
        for number in numbers
    ]
    return sorted_parity


def sort_array_by_parity_one_liner(numbers):
    return [number for number in numbers if number % 2 == 0] + [
        number for number in numbers if number % 2 != 0
    ]

def sort_array_by_parity_one_liner_2(numbers):
    return sorted(numbers, key=lambda x: x & 1)


print(sortArrayByParity([3, 1, 2, 4]))
print(sort_array_by_parity_one_liner([3, 1, 2, 4]))
print(sort_array_by_parity_one_liner_2([3, 1, 2, 4]))

