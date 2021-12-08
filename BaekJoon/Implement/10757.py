a, b = map(str, input().split())

if len(a) != len(b):
    if len(a) < len(b):
        while len(a) != len(b):
            a = '0' + a
    else:
        while len(a) != len(b):
            b = '0' + b

result = []
over = 0
for t_idx in range(len(a)-1, -1, -1):
    a_num = int(a[t_idx])
    b_num = int(b[t_idx])

    temp_result = a_num + b_num + over

    over = temp_result // 10
    temp_result = temp_result % 10

    result.insert(0, str(temp_result))

if over != 0:
    result.insert(0, str(over))

print(''.join(result))