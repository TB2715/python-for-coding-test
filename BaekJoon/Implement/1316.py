test_case = int(input())
input_list = []

count = 0
for _ in range(test_case):
    user_input = input()

    prev_char = ''
    appeared = set()
    isGroup = True
    for char_idx in range(len(user_input)):
        current_char = user_input[char_idx]
        if prev_char == current_char:
            continue
        else:
            # 이전에 등장한 char != 현재 char
            if current_char in appeared:
                isGroup = False
                break
            else:
                # 현재 char가 처음 등장한 경우
                appeared.add(current_char)
                prev_char = current_char

    if isGroup:
        count += 1

print(count)