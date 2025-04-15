N, K = map(int, input().split())

number = input()


removed = 0
selected = []

for num in number:
    num = int(num)
    if not selected:
        selected.append(num)
    else:
        while selected and (selected[-1] < num) and (removed < K):
            selected.pop()
            removed += 1
        selected.append(num)

print("".join(map(str,selected[:(N - K)])))