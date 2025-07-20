if __name__ == "__main__":
    alpha_dict = dict()
    for i in range(26):
        alpha_dict[chr(ord("A") + i)] = 0
    
    N = int(input())

    for _ in range(N):
        word = input()
        for exp, char in enumerate(word[::-1]):
            alpha_dict[char] += 10 ** exp
    
    alpha_list = sorted(zip(alpha_dict.values(), alpha_dict.keys()), reverse=True)
    
    
    max_value = 0
    for i in range(10):
        max_value += alpha_list[i][0] * (9-i)

    print(max_value)