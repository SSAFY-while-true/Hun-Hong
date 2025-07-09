def solution(n, works):
    max_time = max(works)
    remain_works = [0] * (max_time + 1)
    result = 0
    
    for time in works:
        remain_works[time] += 1
    
    while n > 0:
        if max_time < 1:
            break
            
        if remain_works[max_time] > 0:
            remain_works[max_time] -= 1
            remain_works[max_time - 1] += 1
            n -= 1
        else:
            max_time -= 1

    else:
        
        for idx, count in enumerate(remain_works[1:], 1):
            result += (idx ** 2) * count
    
    return result
