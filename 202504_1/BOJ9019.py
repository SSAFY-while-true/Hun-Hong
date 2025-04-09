import sys
input = sys.stdin.readline
from collections import deque


def DSLR_calc(input_num:int, cmd):

    if cmd == "D":
        return (input_num * 2) % 10000
    
    if cmd == "S":
        if input_num == 0:
            return 9999
        else:
            return input_num - 1
    
    if cmd == "L":
        num = (input_num % 1000) * 10 + (input_num // 1000)
        return num

    if cmd == "R":
        num = (input_num // 10) + (input_num % 10) * 1000
        return num


if __name__ == "__main__":
    T = int(input())

    for _ in range(T):
        input_num, out_num = map(int,input().split())
        queue = deque([(input_num, "")])
        visited = set([input_num])

        while queue:
            curr_register, cmd_log = queue.popleft()
            if curr_register == out_num:
                break

            for cmd in "DSLR":
                next_register = DSLR_calc(curr_register, cmd)
                if next_register not in visited:
                    queue.append((next_register, cmd_log + cmd))
                    visited.add(next_register)
        
        print(cmd_log)