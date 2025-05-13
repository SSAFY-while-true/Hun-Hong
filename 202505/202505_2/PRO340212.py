def solution(diffs, times, limit):
    for level in range(min(diffs),min(diffs)+10):
        for i in range(len(diffs)):
            if i == 0:
                tot_time = cal_soltime(level,diffs[0],times[0],0)
            else:
                tot_time += cal_soltime(level,diffs[i],times[i],times[i-1])
        if limit >= tot_time:
            return level
    n=0
    min_level = min(diffs)
    max_level = max(diffs)
    level = (min_level + max_level) // 2
    while True:
        for i in range(len(diffs)):
            if i == 0:
                tot_time = cal_soltime(level,diffs[0],times[0],0)
                tot_time_prev = cal_soltime(level-1,diffs[0],times[0],0)
            else:
                tot_time += cal_soltime(level,diffs[i],times[i],times[i-1])
                tot_time_prev += cal_soltime(level-1,diffs[i],times[i],times[i-1])
        if limit >= tot_time:
            if tot_time_prev > limit:
                break
            else:
                max_level = level
                if max_level-min_level == 1:
                    level = min_level
                else:
                    level = (min_level + level) // 2
        else:
            min_level = level
            if max_level-min_level == 1:
                level = max_level
            else:
                level = (level + max_level) // 2
        n += 1
    return level

def cal_soltime(level,diff,time_cur,time_prev):
    if level == 0:
        return 9999999
    if diff <= level:
        sol_time = time_cur
    else:
        n_try = diff-level
        sol_time = n_try * (time_cur+time_prev) + time_cur
    return sol_time
