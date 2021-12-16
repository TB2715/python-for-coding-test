while True:
    sent = input()
    if sent == '.':
        break

    braket = []
    isPerfect = True
    for char in sent:
        if char == '(' or char == '[':
            braket.append(char)
        elif char == ')':
            if len(braket) == 0:
                isPerfect = False
                break

            if braket[-1] != '(':
                isPerfect = False
                break
            else:
                braket.pop()

        elif char == ']':
            if len(braket) == 0:
                isPerfect = False
                break

            if braket[-1] != '[':
                isPerfect = False
                break
            else:
                braket.pop()

    # [ 혹은 ( 로 마무리 된 경우도 잡기 위해 len() == 0 옵션도 추가
    print('yes') if isPerfect and len(braket) == 0 else print('no')