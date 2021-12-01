def solution(n, lost, reserve):
    hasCloth = [True for i in range(n)]
    hasReserve = ['no' for i in range(n)]

    for idx in lost:
        hasCloth[idx-1] = False
    for idx in reserve:
        if not hasCloth[idx-1]: # 여분을 가지고 있는데 잃어버린 경우
            hasCloth[idx-1] = True
            hasReserve[idx-1] = 'used'
        else:
            hasReserve[idx-1] = 'yes'

    for idx in range(n):
        if not hasCloth[idx]:
            if idx != 0:
                left = hasReserve[idx-1]
                if left=='yes':
                    hasReserve[idx-1] = 'used'
                    hasCloth[idx] = True
                    continue

            if idx != n-1:
                right = hasReserve[idx+1]
                if right=='yes':
                    hasReserve[idx+1] = 'used'
                    hasCloth[idx] = True
                    continue

    print(f'count: {hasCloth.count(True)}')
    answer = hasCloth.count(True)

    return answer


if __name__ == '__main__':
    n = 5
    lost = [1, 2, 4]
    reserve = [1, 3, 5]

    answer = solution(n, lost, reserve)