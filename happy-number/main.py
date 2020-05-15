def test(n):
    previous_numbers = {}
    while True:
        digits = []
        while n > 0:
            remainder = n % 10
            n //= 10
            digits.append(remainder)

        squared = [digit ** 2 for digit in digits]
        n = sum(squared)
        if n in previous_numbers:
            return False
        previous_numbers[n] = True
        if sum(squared) == 1:
            return True


test(20)
