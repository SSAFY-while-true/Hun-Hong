import sys
input = sys.stdin.readline


def two_pt_sum(N, left_pt, right_pt, metric):

    min_metric = float("Inf")

    if metric[0] > 0:
        return (metric[left_pt], metric[left_pt + 1])
    if metric[N - 1] < 0:
        return (metric[right_pt - 1], metric[right_pt])

    while left_pt != right_pt:

        cur_metric = metric[left_pt] + metric[right_pt]
        
        if min_metric >= abs(cur_metric):
            min_metric =  abs(cur_metric)
            result = (metric[left_pt], metric[right_pt])

        if min_metric == 0:
            break

        if cur_metric > 0:
            right_pt -= 1
        else:
            left_pt += 1
        
    return (result)


if __name__ == "__main__":
    N = int(input())

    metric = list(map(int, input().split()))

    left_pt = 0
    right_pt = N - 1

    print(*two_pt_sum(N, left_pt, right_pt, metric))
