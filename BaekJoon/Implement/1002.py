import math

test_count = int(input())

for _ in range(test_count):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())

    # 경우의 수
    # 1. 외접, 내접 -> dot = 1
    # 2. 거리가 멀거나, 내부에 위치할 경우 -> dot = 0
    # 3. 겹칠 경우 -> dot =2

    # Step 1. 두 원의 거리를 계산
    # (x-a)^2 + (y-b)^2 = r^2
    distance = (x2-x1)**2 + (y2-y1)**2
    distance = math.sqrt(distance)

    # Step 2. 중심 거리와 두 원의 위치 관계식을 이용, 접점의 개수를 구함
    if distance == 0 and r1 == r2: # 두 원이 동심원이고, 반지름이 같은 경우
        print(-1)
    elif abs(r1-r2) == distance or r1 + r2 == distance: # 내/외접일때
        print(1)
    elif abs(r1-r2) < distance < (r1+r2): # 두 원이 서로 다른 두 점에서 만날 때
        print(2)
    else:
        print(0)

# 참고: https://ooyoung.tistory.com/111