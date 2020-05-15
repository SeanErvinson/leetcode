def test(c):
    jumps = -1
    index = 0
    while index < len(c):
        jumps+=1
        if index<len(c)-2 and c[index+2]==0:
            index+=1
        index+=1
    print(jumps)

test([0,0,1,0,0,1,0])
