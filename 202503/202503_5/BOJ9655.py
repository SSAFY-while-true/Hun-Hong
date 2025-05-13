import sys
input = sys.stdin.readline


if __name__ == "__main__":
    N = int(input())

    if N % 4 == 0 or N % 4 == 2:
        print("CY")
    else:
        print("SK")
