test_count = int(input())

# XX(나머지) + YY(몫)
# if XX == 0: XX = h
# if YY < 10: YY = '0' + YY

for _ in range(test_count):
    h, w, n = map(int, input().split())

    XX = n % h
    if XX == 0:
        XX = str(h)
        YY = n//h
    else:
        XX = str(XX)
        YY = (n // h) + 1

    if YY < 10:
        YY = '0' + str(YY)
    else:
        YY = str(YY)

    print(XX + YY)