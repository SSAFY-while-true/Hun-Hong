n, d = map(int, input().split())

family = list(map(int, input().split()))
adj_list = [[] * (n + 1) for _ in range(n + 1)]

for idx, father in enumerate(family):
    adj_list[father].append(idx)

# 재귀를 이용하여 반복적으로 선조를 할당하는 함수
# ex)
# 7 2
# 0 0 0 0 0 0 0
def how_many_add(number_father, limit):
    additional = 0
    if number_father > limit:
        remain = number_father // limit
        if remain > limit:
            additional += how_many_add(remain, limit) + how_many_add(number_father - remain, limit)
            additional += limit
        else:
            additional += remain
    return additional


additional = 0
for row in adj_list:
    additional += how_many_add(len(row), d)
    #print(len(row))

print(additional)



