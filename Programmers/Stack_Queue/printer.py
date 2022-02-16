from collections import deque

def solution(priorities, location):
    queue = deque([idx, a_p] for idx, a_p in enumerate(priorities))

    count = 0
    while True:
        a_idx, a_priority = queue.popleft()

        is_high = True
        for p_item in queue:
            if a_priority < p_item[1]:
                queue.append([a_idx, a_priority])
                is_high = False
                break

        if is_high:
            count += 1
            if a_idx == location:
                return count



if __name__ == '__main__':
    priorities = [1, 1, 9, 1, 1, 1]
    location = 0
    solution(priorities, location)