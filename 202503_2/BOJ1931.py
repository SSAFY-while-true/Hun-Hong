import sys
input = sys.stdin.readline


if __name__ == "__main__":
    N = int(input())

    meetings = [tuple(map(int, input().split())) for _ in range(N)]
    meetings.sort(key=lambda x:x[0])
    meetings.sort(key=lambda x:x[1])
    end_time = 0
    meeting_count = 0

    for meeting in meetings:
        if end_time <= meeting[0]:
            end_time = meeting[1]
            meeting_count += 1
    
    print(meeting_count)