def solution(words, queries):
    answer = []
    for keyword in queries:

        # ?의 위치 및 범위 찾기
        start = keyword.index('?')
        end = 0
        for idx, char in enumerate(keyword[start:]):
            if char == '?':
                continue
            else:
                end = start + idx
                break
        if end == 0:
            end = len(keyword) - 1

        if start == 0:
            splited_keyword = keyword[end:]
        else:
            splited_keyword = keyword[:start]

        count = 0
        for a_word in words:
            if len(a_word) != len(keyword):
                continue

            if start == 0:
                if splited_keyword == a_word[end:]:
                    count += 1
            else:
                if splited_keyword == a_word[:start]:
                    count += 1

        answer.append(count)
    return answer


if __name__ == '__main__':
    words = ["frodo", "front", "frost", "frozen", "frame", "kakao"]
    queries = ["fro??", "????o", "fr???", "fro???", "pro?"]
    print(solution(words, queries))
