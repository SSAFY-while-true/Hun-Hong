N, r, c = map(int, input().split())


count = 0 
for i in range(N - 1, -1, -1):
    r_div = r // (2 ** i) # 1
    c_div = c // (2 ** i) # 0

    r %= (2 ** i)
    c %= (2 ** i)

    if (r_div, c_div) == (0, 1):
        count += ((2 ** i) ** 2) * 1
    elif (r_div, c_div) == (1, 0):
        count += ((2 ** i) ** 2) * 2
    elif (r_div, c_div) == (1, 1):
        count += ((2 ** i) ** 2) * 3
    

print(count)

