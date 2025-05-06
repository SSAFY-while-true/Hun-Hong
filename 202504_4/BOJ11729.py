def hanoi_recursive(number, start, destination):
    global position, K, order
    if number < 1:
        return
    if start == destination:
        return
    
    if start == 1:
        if destination == 2:
            hanoi_recursive(number-1, position[number], 3)
        else:
            hanoi_recursive(number-1, position[number], 2)

    elif start == 2:
        if destination == 1:
            hanoi_recursive(number-1, position[number], 3)
        else:
            hanoi_recursive(number-1, position[number], 1)

    elif start == 3:
        if destination == 1:
            hanoi_recursive(number-1, position[number], 2)
        else:
            hanoi_recursive(number-1, position[number], 1)        


    # print(start, destination)
    order.append((start, destination))
    position[number]=destination
    
    hanoi_recursive(number-1, position[number-1], destination)
    K += 1

if __name__ == "__main__":
    N = int(input())
    order = []
    K = 0
    position = [1] * (N + 1)
    hanoi_recursive(N, 1, 3)
    print(K)
    for s, d in order:
        print(s, d)