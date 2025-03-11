def solution(players, m, k):
    server = 1
    count = 0
    queue = []
    
    for player in players:
        while player >= m * server:
            server += 1
            queue.append(k)
            count += 1
        
        for idx in range(len(queue) - 1, -1, -1):
            queue[idx] -= 1
            if queue[idx] == 0:
                queue.pop(idx)
                server -= 1
            
    return count