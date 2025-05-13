def alphary(input_string: str):
    # a : 1, b : 1 ... z : 25
    number = 0
    for digit, char in enumerate(input_string[::-1]):
        number += (26 ** digit) * (ord(char) - ord('a') + 1)
    return number


def inverse_alphary(input_int: int):
    # 1: a, 2: b ... z: 26
    out_string = ""
    while input_int > 0:
        digit = (input_int - 1) % 26
        input_int = (input_int - 1) // 26
        
        out_string = chr(digit + ord('a')) + out_string
    
    return out_string


def solution(n, bans):
    ban_int = list(map(alphary, bans))
    ban_int.sort()
    
    for ban in ban_int:
        if ban <= n:
            n += 1
    
    return inverse_alphary(n)
    