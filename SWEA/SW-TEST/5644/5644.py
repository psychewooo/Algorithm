# [SWEA / 모의 SW 역량 테스트] 5644. 무선 충전

# import sys
# sys.stdin = open('sample_input.txt')

# 인덱스와 숫자를 맞추어 이동 방향 정의 (이동하지 않음, 상우하좌)
dx = [0, 0, 1, 0, -1]
dy = [0, -1, 0, 1, 0]


def is_possible(x1, y1, x2, y2, c):
    """
    현재 위치와 BC의 거리를 구하여
    BC에의 접속 가능 여부를 판단하는 함수

    (x1, y1) = 사용자의 현 위치
    (x2, y2) = BC의 위치
    c = 충전 범위
    
    True: 접속 가능
    False: 접속 불가능
    """
    # 두 지점사이의 거리 
    distance = abs(x1 - x2) + abs(y1 - y2)

    # 충전 범위 안에 드나요?
    if distance <= c:
        return True
    
    else:
        return False


def charge(M, A, move_a, move_b, info):
    """
    무선 충전의 범위와 사용자의 이동 궤적이 주어졌을 때,
    모든 사용자가 충전한 양의 최댓값을 반환하는 함수
    """

    # 사용자의 출발 위치
    user_a = [1, 1]
    user_b = [10, 10]

    # 현재 시간 (초)
    s = 0

    # 모든 사용자의 충전량 합
    total = 0

    # 주어진 총 이동 시간까지 탐색 반복
    while s < M + 1:

        # 현 위치에서 충전 가능한 BC의 목록
        # '-1': 충전 불가능
        battery_a = [-1]
        battery_b = [-1]

        for i, bc in enumerate(info):
            # BC의 좌표, 충전 범위, 처리량
            bc_x, bc_y, c, p = bc[0], bc[1], bc[2], bc[3]

            # 함수 호출: 접속 가능한가요?
            if is_possible(user_a[0], user_a[1], bc_x, bc_y, c):
                battery_a.append(i)
            
            if is_possible(user_b[0], user_b[1], bc_x, bc_y, c):
                battery_b.append(i) 
 
        max_charge = 0

        # for 문을 통한 조합 구현으로 충전기 고르기
        for i in battery_a:
            for j in battery_b:
                current_charge = 0

								# 충전 가능한 BC가 없으면 충전량은 0, 그렇지 않으면 처리량 가져오기
                Pi = info[i][3] if i != -1 else 0
                Pj = info[j][3] if j != -1 else 0

                # 사용자가 충전 가능한 BC가 동일할 때
                if i == j and i != -1:
		                # 둘은 처리량을 절반 나누어 가지므로 그 값은 총량과 같다
                    current_charge = Pi    # Pj라고 적어도 됨
                
                # 두 사용자가 충전 가능한 BC가 다르거나, 둘 or 둘 중 한 명이 충전 가능한 BC가 없을 때
                else:
                    current_charge = Pi + Pj

                max_charge = max(max_charge, current_charge)
        
        # 최대 충전값을 충전량에 더해주기
        total += max_charge

        if s < M:
            # 다음 위치로 사용자 이동
            user_a[0] += dx[move_a[s]]    # x 좌표
            user_a[1] += dy[move_a[s]]    # y 좌표
        
            user_b[0] += dx[move_b[s]]
            user_b[1] += dy[move_b[s]]

        # 시간 증가
        s += 1
    
    return total


T = int(input())

for tc in range(1, T + 1):
    # 총 이동 시간 M, BC의 개수 A
    M, A = map(int, input().split())

    # 사용자의 이동 정보
    move_a = list(map(int, input().split()))
    move_b = list(map(int, input().split()))

    info = []

    for _ in range(A):
        # 좌표, 충전 범위 C, 처리량 P
        x, y, C, P = list(map(int, input().split()))
        info.append([x, y, C, P])

		# 함수 호출
    print(f'#{tc} {charge(M, A, move_a, move_b, info)}')