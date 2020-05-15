import collections
def test(n, ar):
    colors = {}
    pair = 0
    for i in range(0, n):
        sock = ar[i]
        # if sock not in colors:
        #     colors[sock]=colors.get(sock, 0) + 1
        # else:
        #     pair+=1
        #     colors.pop(sock, None)
        colors[sock] = colors.get(sock, 0) + 1
        if colors[sock] == 2:
            pair+=1
            colors[sock] = 0


    print(pair)

test(11,[10,20,20,10,10,30,50,10,20,10,10])