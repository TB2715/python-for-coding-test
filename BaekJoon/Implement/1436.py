n = int(input())

count = 0

c_num = 666

while True:
    if '666' in str(c_num):
        count += 1

        if count == n:
            print(c_num)
            break

    c_num += 1