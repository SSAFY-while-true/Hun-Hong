from collections import deque
from copy import deepcopy
N = int(input())

int_list = deque(list(map(int, input().split())))

operator = list(map(int, input().split()))

min_value = float("Inf")
max_value = float("-Inf")

def tracking(int_list: deque, operator, acc=0):
    global min_value, max_value
    if sum(operator) > 0:

        for i in range(4):
            n_int_list = deepcopy(int_list)
            n_operator = deepcopy(operator)
            left = n_int_list.popleft()
            right = n_int_list.popleft()
            if n_operator[i] > 0:
                if i==0:
                    acc = left + right
                elif i==1:
                    acc = left - right
                elif i==2:
                    acc = (left * right)
                elif i==3:
                    if left > 0:
                        acc = (left // right)
                    else:
                        left = -left
                        acc = -(left // right)
                n_operator[i] -= 1
                #print(acc)
                n_int_list.appendleft(acc)
                tracking(n_int_list, n_operator, acc)
    else:
        acc = int_list.popleft()
        if min_value > acc:
            min_value = acc
        if max_value < acc:
            max_value = acc
    
tracking(int_list, operator)

print(max_value)
print(min_value)
