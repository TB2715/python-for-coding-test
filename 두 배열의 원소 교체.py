N, K = map(int, input().split())

list_a = list(map(int, input().split()))
list_b = list(map(int, input().split()))

for _ in range(K):
    a_min_idx = list_a.index(min(list_a)) # A의 가장 작은 값의 index
    b_max_idx = list_b.index(max(list_b)) # B의 가장 큰 값의 index

    list_a[a_min_idx] = max(list_b) # A의 가장 작은 값을 B의 가장 큰 값으로 변경
    list_b.pop(b_max_idx) # B에서 해당 값 삭제

print(sum(list_a))