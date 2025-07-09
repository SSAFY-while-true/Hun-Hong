if __name__ == "__main__":
    N = int(input())

    tops = list(map(int, input().split()))
    recievers = [0] * N
    stack = []

    for idx, top in enumerate(tops):
        if not stack:
            stack.append((idx, top))
            continue

        while stack and stack[-1][1] < top:
            stack.pop()
            
        if stack:
            recievers[idx] = stack[-1][0] + 1
        else:
            recievers[idx] = 0
        
        stack.append((idx, top))
        
    print(" ".join(map(str, recievers)))