def add_fish():
    min_idx = []
    min_value = float("Inf")

    for idx, fish in enumerate(fishes[-1]):
        if fish == min_value:
            min_idx.append(idx)
        elif fish < min_value:
            min_value = fish
            min_idx = [idx]

    for idx in min_idx:
        fishes[-1][idx] += 1
    
    return


def left_up():
    fishes[-2][0] = fishes[-1][0]
    fishes[-1][:] = fishes[-1][1:] + [0]

def rotate_90():
    min_idx = -1
    for fish in fishes[-2]:
        if fish:
            min_idx += 1
        else:
            break
    zip(fishes[min_idx])



if __name__ == "__main__":
    '''
    8 7
    
    '''
    # N, K = map(int, input().split())
    N, K = 8, 7
    fishes = [[0] * N for _ in range(N)]
    inp = "5 2 3 14 9 2 11 8"
    fishes[-1] = list(map(int, inp.split()))
    # fishes[-1] = list(map(int, input().split()))

    from pprint import pprint
    pprint(fishes)

    add_fish()
    pprint(fishes)

    left_up()
    pprint(fishes)

    rotate_90()