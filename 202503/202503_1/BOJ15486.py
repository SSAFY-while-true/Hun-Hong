import sys
input = sys.stdin.readline

N = int(input())

T_list = [0]
P_list = [0]

for i in range(N):
    T, P = map(int, input().split())
    T_list.append(T)
    P_list.append(P)

# dp는 뒤에서 그날까지 얻을 수 있는 최대 보수
# index에러를 처리하기 위해 range를 N + 2로 설정
dp = [0] * (N + 2)

# N일 부터 1일 까지 순회하면서
# day(현재 날짜) + T_list[day](걸리는 기간) - 1이 퇴사 날짜인 N보다 크다면
# 상담이 불가능하므로 dp는 업데이트 되지 않음
for day in range(N, 0, -1):
    if day + T_list[day] - 1 > N:
        # 같은 dp를 할당
        dp[day] = dp[day + 1]
    else:
        # dp는 현재 보수인 P_list[day]와 
        # T일 후 보수 dp[day + T_list[day]]를 더한 값과
        # 바로 다음 날의 보수 중 더 높은 값을 가져가야함
            dp[day] = max(P_list[day] + dp[day + T_list[day]], dp[day + 1])

# 1일째의 dp를 출력
print(dp[1])