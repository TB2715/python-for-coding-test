from collections import deque

t = int(input())

for _ in range(t):
    ui = input()
    bracket = []
    for a_b in ui:
        if a_b == '(':
            bracket.append(a_b)
        else:
            if len(bracket) == 0:
                bracket.append(a_b)
                continue
            elif bracket[-1] == '(':
                bracket.pop()
            else:
                bracket.append(a_b)

    print('YES') if len(bracket) == 0 else print('NO')