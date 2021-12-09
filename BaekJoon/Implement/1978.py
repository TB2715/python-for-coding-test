# 소수: 1보다 큰 자연수에서 1과 자기 자신을 제외한 자연수로는 나누어 떨어지지 않는 자연수

"""
약수의 성질
가운데 약수를 기준으로 곱셈 연산에 대해 대칭을 이룸
-> 특정 자연수의 모든 약수를 찾을 때 가운데 약수(제곱근)까지만 확인

"""

# import math
#
# def is_prime_number(x):
#     for i in range(2, int(math.sqrt(x))+ 1):
#         # 2부터 x의 제곱근까지의 모든 수를 확인
#         if x % i == 0:
#             return False # 소수가 아님
#     return True
import math

n = int(input())
numbers = input().split()
numbers = [int(n) for n in numbers]

count = 0
for a_num in numbers:
    isPN = True

    for i in range(2, int(math.sqrt(a_num))+1):
        if a_num % i == 0:
            isPN = False
            break

    if a_num == 1:
        isPN = False

    if isPN:
        count += 1

print(count)