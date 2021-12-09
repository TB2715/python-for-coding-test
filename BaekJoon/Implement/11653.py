n = int(input())

left = n
while left > 1:
    for i in range(2, n+1):
        if left % i == 0:
            print(i)
            left //= i
            break