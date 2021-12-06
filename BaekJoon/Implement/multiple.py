first = int(input())
second = input()

result = []
for num_in_second in reversed(second):
    print(first * int(num_in_second))

print(first * int(second))