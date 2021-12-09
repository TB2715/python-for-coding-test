n = int(input())

for num in range(n+1):
    temp_sum = sum([int(x) for x in str(num)]) + num

    if n == temp_sum:
        print(num)
        quit()

print(0)

