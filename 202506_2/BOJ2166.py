if __name__ == "__main__":
    # import sys
    # input = sys.stdin.readline

    N = int(input())

    ## 풀이 전략
    # 신발끈 공식(벡터의 외적을 이용한 방법)
    # S = abs(x1 x y2 - x2 x y1 + x2 x y3 - x3 x y2 ... + xn x y1 - x1 x yn) / 2

    S = 0
    x_0, y_0 = map(int, input().split())

    x_before, y_before = x_0, y_0

    for _ in range(1, N):
        x_next, y_next = map(int, input().split())
        S += (x_before * y_next) - (x_next * y_before)
        x_before, y_before = x_next, y_next
    
    S += (x_before * y_0) - (x_0 * y_before)

    print(round(abs(S) / 2, 1))