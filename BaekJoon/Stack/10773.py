k = int(input())

history = []

for _ in range(k):
    ui = int(input())

    if ui == 0:
        history.pop()
    else:
        history.append(ui)

print(sum(history))