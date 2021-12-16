# import sys
# input = sys.stdin.readline
#
# n = int(input())
#
# stack = []
# for _ in range(n):
#     order = input().rstrip()
#
#     if order[:4] == 'push':
#         num = order.split(' ')[1]
#         stack.append(num)
#
#     elif order == 'pop':
#         if len(stack) == 0:
#             print('-1')
#         else:
#             print(stack[-1])
#             stack.pop()
#
#     elif order == 'size':
#         print(len(stack))
#
#     elif order == 'empty':
#         print('0') if len(stack)>0 else print('1')
#
#     elif order == 'top':
#         print(stack[-1])
#
#     else:
#         print('ERROR')

import sys
input=sys.stdin.readline

n = int(input()) #명령의 수
stack=[]

def push(x):
    #리스트의 마지막에 추가
    stack.append(x) #딱히 int(x)할 필요는 없을 듯

def pop():
    if(len(stack)==0):
        print(-1)
    else:
        print(stack.pop())

def size():
    print(len(stack))

def empty():
    if(len(stack)==0): #비면
        print(1)
    else: #안 비면
        print(0)

def top():
    if(len(stack)==0):
        print(-1)
    else:
        print(stack[-1])


for i in range(n):
    command=input().split() #push 1 같은 애들 분리
    if(command[0] == 'push'):
        push(command[1])
    if (command[0] == 'pop'):
        pop()
    if (command[0] == 'size'):
        size()
    if (command[0] == 'empty'):
        empty()
    if (command[0] == 'top'):
        top()