from itertools import combinations

if __name__ == "__main__":
    N, K = map(int, input().split())

    essential_words = ['a', 'n', 't', 'i', 'c']
    result = 0
    words_bin = 0b0
    essential_bin = 0b0

    for word in essential_words:
        essential_bin |= 1 << (ord(word) - ord('a'))

    words_bin = essential_bin

    words = [input() for _ in range(N)]
    word_bins = []

    if K < 5:
        result = 0
    elif K == 26:
        result = N
    else:
        for word in words:
            bins = 0
            for char in word:
                bins |= 1 << (ord(char) - ord('a'))
                words_bin |= 1 << (ord(char) - ord('a'))
            
            word_bins.append(bins)
    
        additional_word = words_bin & ~essential_bin
        add_idx = []
        for idx, word in enumerate(format(additional_word, "#b")[::-1]):
            if word == "1":
                add_idx.append(idx)

        if len(add_idx) < K - 5:
            result = N
        else: 
            for comb in combinations(add_idx, K - 5):
                know_word = 0b0
                cur_result = N
                for num in comb:
                    know_word |= 1 << num
                know_word |= essential_bin

                for bins in word_bins:
                    if bins & ~know_word != 0:
                        cur_result -= 1

                    if cur_result < result:
                        break
                else:
                    result = cur_result
    
    print(result)