# 1
# 7 + 6
# 19 + 12 (6*2)
# 37 + 18 (6*3)
# 61 + 24 (6*4)

n = int(input())

six = 0
sum = 1
while True:
    sum += six * 6
    if n <= sum:
        print(six + 1)
        break
    six += 1
