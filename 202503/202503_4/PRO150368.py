from itertools import product


def solution(users, emoticons):
    N = len(emoticons)

    max_income = 0
    max_plus = 0

    for i in product([10, 20, 30, 40], repeat=N):
        plus = 0
        income = 0
        for user in users:
            plus += (sum([emoticon * (100 - i[idx]) / 100 for idx, emoticon in enumerate(emoticons) if i[idx] >= user[0]])) >= user[1]

            if not (sum([emoticon * (100 - i[idx]) / 100 for idx, emoticon in enumerate(emoticons) if i[idx] >= user[0]])) >= user[1]:
                income += sum([emoticon * (100 - i[idx]) / 100 for idx, emoticon in enumerate(emoticons) if i[idx] >= user[0]])


        if max_plus < plus:
            max_plus = plus
            max_income = income
        elif max_plus == plus:
            if max_income < income:
                max_income = income

    return [max_plus, max_income]