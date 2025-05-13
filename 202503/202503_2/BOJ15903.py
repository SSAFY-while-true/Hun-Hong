import sys
input = sys.stdin.readline

if __name__ == "__main__":
    n, m = map(int, input().split())

    cards = list(map(int, input().split()))

    # print(cards)
    n_merge = 0
    while n_merge < m:
        cards.sort()
        cards[0], cards[1] = cards[0] + cards[1], cards[0] + cards[1]
        n_merge += 1
    
    print(sum(cards))