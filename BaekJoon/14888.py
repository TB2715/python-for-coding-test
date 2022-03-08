import sys

N = int(input())
num_list = list(map(int, input().split()))
operator_list = list(map(int, input().split()))  # 덧셈, 뺄셈, 곱셈, 나눗셈의 개수

maximum = -(sys.maxsize + 1)
minimum = sys.maxsize


def dfs(depth, total, plus_count, minus_count, multiply_count, divide_count):
    global maximum, minimum

    if depth == N:
        maximum = max(total, maximum)
        minimum = min(total, minimum)

        return

    if plus_count:
        dfs(depth + 1, total + num_list[depth], plus_count - 1, minus_count, multiply_count, divide_count)

    if minus_count:
        dfs(depth + 1, total - num_list[depth], plus_count, minus_count - 1, multiply_count, divide_count)

    if multiply_count:
        dfs(depth + 1, total * num_list[depth], plus_count, minus_count, multiply_count - 1, divide_count)

    if divide_count:
        if total < 0:
            dfs(depth + 1, -1 * (abs(total) // num_list[depth]), plus_count, minus_count, multiply_count, divide_count - 1)
        else:
            dfs(depth + 1, total // num_list[depth], plus_count, minus_count, multiply_count, divide_count - 1)


dfs(1, num_list[0], operator_list[0], operator_list[1], operator_list[2], operator_list[3])
print(maximum)
print(minimum)


'''
최대: 
 * 곱하기: 제일 큰 수 
 * 나누기: 제일 작은 수 % 그 다음 작은 수 
 * 빼기: 그 다음 작은 수
 * 더하기: 나머지... 
 
 라고 생각했는데,... 그냥 모든 경우의 수를 구하는 것 같다 
'''
