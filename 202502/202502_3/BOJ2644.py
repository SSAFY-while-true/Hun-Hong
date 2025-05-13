import sys
input = sys.stdin.readline

n_human = int(input())

p_start, p_end = map(int, input().split())
m = int(input())
adj_matrix = [[0] * (n_human + 1) for _ in range(n_human + 1)]
visited = [False] * (n_human + 1)
for _ in range(m):
    one, two = map(int, input().split())
    adj_matrix[one][two] = 1
    adj_matrix[two][one] = 1

distance = -1
count = 0
stack = [(p_start, count)]
visited[p_start] = True

while stack:
    curr, curr_count = stack.pop()
    if curr == p_end:
        distance = curr_count
        break

    curr_count += 1
    for p_next in range(n_human, 0 , -1):
        if adj_matrix[curr][p_next] == 1 and not visited[p_next]:
            stack.append((p_next, curr_count))
            visited[p_next] = True

print(distance)