if __name__ == "__main__":
    N = int(input())
    B = list(map(int, input().split()))
    count = 0

    while sum(B) != 0:
        for idx, number in enumerate(B):
            if number % 2 == 1:
                B[idx] -= 1
                break

        else:
            for idx, _ in enumerate(B):
                B[idx] //= 2
    
    print(count)