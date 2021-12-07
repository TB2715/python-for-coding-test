count = int(input())

for _ in range(count):
    ox_result = input()

    sum = 0
    o_count = 0
    for ox in ox_result:
        if ox == 'O':
            o_count += 1
            sum += o_count
        else:
            o_count = 0

    print(sum)