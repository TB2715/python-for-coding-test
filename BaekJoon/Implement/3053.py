import math

user_input = int(input())

# 원의 넓이: R^2 * 3.14
print(f'{user_input * user_input * math.pi:.6f}')

# 택시 기하학: 높이가 R인 직각삼각형 4개의 넓이(마름모꼴)
print(f'{((user_input * user_input)/2) * 4:.6f}')
