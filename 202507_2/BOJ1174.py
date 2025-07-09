from itertools import combinations

if __name__ == "__main__":
    N = int(input())
    
    decrease_numbers = []
    digits = list(range(9, -1, -1))
    for len_digit in range(1, 11):
        for comb in combinations(digits, len_digit):
            decrease_numbers.append(sum([digit * (10 ** (len(comb)-exp)) 
                                     for exp, digit in enumerate(comb, 1)]))

    if N > len(decrease_numbers):
        print(-1)
    else:
        print(sorted(decrease_numbers)[N - 1])