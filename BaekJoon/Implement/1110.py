n = list(input())

if len(n) < 2:
    n.insert(0, '0')

count = 1
new_n = n[1] + str((int(n[0]) + int(n[1])) % 10)

while int(new_n) != int(''.join(n)):
    temp_sum = int(new_n[0]) + int(new_n[1])

    new_n = new_n[1] + str(temp_sum % 10)
    count += 1
print(count)