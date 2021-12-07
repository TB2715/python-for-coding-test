test_case_count = int(input())


for _ in range(test_case_count):
    repeat, sent = input().split()

    result = ''
    for s in sent:
        result += s * int(repeat)

    print(result)