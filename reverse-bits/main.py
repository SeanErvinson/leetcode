def test(n: int):
    bits = bin(n)[2:]
    return int(bits.zfill(32)[::-1], 2)


print(test(int("00000000000000000000000000000001", 2)))
print(test(int("00000010100101000001111010011100", 2)))
print(test(int("11111111111111111111111111111101", 2)))

