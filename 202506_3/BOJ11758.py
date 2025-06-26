if __name__ == "__main__":
    p1_x, p1_y = map(int, input().split())
    p2_x, p2_y = map(int, input().split())
    p3_x, p3_y = map(int, input().split())

    p21_x = p2_x - p1_x
    p21_y = p2_y - p1_y

    p32_x = p3_x - p2_x
    p32_y = p3_y - p2_y

    cross_prod = (p21_x * p32_y - p21_y * p32_x)

    if cross_prod > 0:
        print(1)
    elif cross_prod < 0:
        print(-1)
    else:
        print(0)


    