def old_solution(name):
    count = 0
    second_idx = 0
    last_idx = 0
    before_a_idx = 0
    a_legth = 0

    for cidx, char in enumerate(name):
        if char == 'A':
            continue
        else:
            temp_count = ord(name[cidx]) - ord('A')

            if temp_count > 13:
                temp_count = ord('Z') - ord(name[cidx]) + 1

            count += temp_count
            last_idx = cidx

        if cidx != 0 and second_idx == 0:
            second_idx = cidx

    if len(name) // 2 < second_idx:
        count += len(name) - second_idx
    else:
        count += last_idx

    answer = count
    return answer


def solution(name):
    move_history_list = []

    for char_idx, a_char in enumerate(name):

        # 알파벳 위 아래 이동 count
        temp_count = ord(name[char_idx]) - ord('A')

        if temp_count > 13:
            temp_count = ord('Z') - ord(name[char_idx]) + 1

        move_history_list.append(temp_count)

    start_idx = 0
    end_idx = 0
    long_a_info = [0, 0, 0]
    prev_count = -1
    for h_idx, move_count in enumerate(move_history_list):
        if prev_count != 0 and move_count == 0:
            start_idx = h_idx
        elif prev_count == 0 and move_count != 0:
            end_idx = h_idx - 1
            a_length = end_idx - start_idx + 1

            if a_length > long_a_info[2]:
                long_a_info = [start_idx, end_idx, a_length]
        prev_count = move_count

    count = len(name) - (long_a_info[2] + 1) + (long_a_info[0] - 1)
    count += sum(move_history_list)

    return count


# 'A'부터 원하는 문자를 찾는데까지 조이스틱을 상하로 이동한 횟수 구함
# '위'로 이동 vs '아래'로 이동 -> 비교 후 작은 count 반환
def find_move_up_down(name_char):
    return min(ord(name_char) - ord('A'), ord('Z') - ord(name_char) + 1)


# 현재 위치부터 왼/오른쪽으로 이동하면서 변경이 필요한 문자까지 이동한 거리를 반환
# 더 이상 변경이 필요한 문자가 없을 경우 0을 반환
def find_move_left_right(count_list: list, current_idx: int, direction: int):
    count = 0

    while count < len(count_list):
        count += 1
        current_idx += direction

        if current_idx == len(count_list): # 오른쪽으로 진행하면서 index가 over될 경우
            current_idx = 0

        if count_list[current_idx] != 0:  # 바꿔야할 문자를 발견
            return count

    return 0


def other_solution(name):
    answer = 0
    count_list = []

    # 알파벳 상하 이동 count 계산
    for a_char in name:
        count_list.append(find_move_up_down(a_char))

    start = 0
    while True:
        answer += count_list[start]  # 현재 위치 문자를 변경하는데 필요한 조이스틱의 상하 이동 횟수를 추가
        count_list[start] = 0  # 현재 위치 문자 변경 완료 -> 상하 필요 횟수 0으로 초기화

        left_move = find_move_left_right(count_list, start, -1)
        right_move = find_move_left_right(count_list, start, 1)

        if left_move == 0 and right_move == 0:
            break

        if left_move < right_move:
            if start - left_move >= 0:
                start -= left_move
            else:
                start = len(count_list) - (left_move - start)
            answer += left_move
        else:
            if start + right_move < len(count_list):
                start += right_move
            else:
                start = right_move - (len(count_list) - start)
            answer += right_move

    return answer


if __name__ == '__main__':
    test_case = ['ZAZZ', 'JAN', 'JAJAAAJ', 'JEROEN', ]
    answer_list = [5, 23, 31, 56]

    for tidx, a_test in enumerate(test_case):
        name = a_test
        answer = other_solution(name)
        print(f'{answer == answer_list[tidx]} // result: {answer} / answer: {answer_list[tidx]}')
