from collections import deque

def solution(progrsses, speeds):
    answer = []

    queue = deque([[idx, p] for idx, p in enumerate(progrsses)])

    while queue:
        for q_idx in range(len(queue)):
            queue[q_idx][1] += speeds[queue[q_idx][0]]

        count = 0
        while queue and queue[0][1] >= 100:
            count+=1
            queue.popleft()

        if count > 0:
            answer.append(count)

    return answer


if __name__ == '__main__':
    progresses = [93, 30, 55]
    speeds = [1, 30, 5]
    solution(progresses, speeds)