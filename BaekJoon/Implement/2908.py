first, second = map(int, input().split())

reversed_first = ''
reversed_second = ''
for x in reversed(str(first)):
    reversed_first += x
for y in reversed(str(second)):
    reversed_second += y

if int(reversed_first) > int(reversed_second):
    print(int(reversed_first))
else:
    print(int(reversed_second))
