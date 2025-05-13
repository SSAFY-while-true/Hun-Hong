def is_handle(n, times, total_time):
    handled = 0
    for time in times:
        handled += total_time // time
    
    return handled >= n


def solution(n, times):
    left = 0
    right = n * max(times)
    
    while right - left > 1:
        mid = (left + right) // 2
        if is_handle(n, times, mid):
            right = mid
        else:
            left = mid
    
    if is_handle(n, times, left):
        answer = left
    else:
        answer = right
        
    return answer