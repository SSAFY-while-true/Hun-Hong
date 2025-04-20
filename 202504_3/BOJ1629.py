def recusive_multi(number, count, divider):
    global memo
    if memo.get(count):
        return memo[count]
    
    if count > 2:
        result = (recusive_multi(number, count // 2, divider) * recusive_multi(number, count - (count // 2), divider)) % divider
        memo[count] = result
        return result
    elif count == 2:
        memo[count] = number ** 2
        return (number ** 2) % divider
    else:
        memo[count] = number
        return (number) % divider

if __name__ == "__main__":
    A, B, C = map(int, input().split())
    memo = dict()

    print(recusive_multi(A, B, C))