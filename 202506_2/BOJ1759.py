def comb_recursive(L, password='', start_idx=0):
    global pass_list, pass_alpha

    if len(password) == L:
        num_vowels = sum([1 for char in password if char in vowels])
        if num_vowels >= 1 and L - num_vowels >= 2:
            pass_list.append(password)

        return
    
    # print(password)
    for idx, char in enumerate(pass_alpha[start_idx:], start_idx):

        comb_recursive(L, password + char, idx + 1)



if __name__ == "__main__":

    vowels = {"a", "e", "i", "o", "u"}

    L, C = map(int, input().split())

    pass_alpha = list(input().split())
    pass_alpha.sort()

    pass_list = []

    comb_recursive(L)

    for password in pass_list:
        print(password)