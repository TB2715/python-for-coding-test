def dfs(array, numbers, target: int, size: int):
    answer = 0

    if len(array) == size and sum(array) == target:
        return 1





def solution(numbers:list, target:int):
    answer = 0
    answer += dfs([numbers[0]], numbers[1:], target, len(numbers))