n = int(input())

triangle = []

# for idx in range(n):
#     # 1, 3, 5, 7, ... (2n + 1)
#     # 0, 1, 2, 3, ... (n)
# 
#     width = 2 * idx + 1
#     space_count = idx
# 
#     a_line = [0] * width
#     input_list = list(map(int, input()))
#     lidx = 0
#     for widx in range(width):
#         if widx % 2 == 0:
#             continue
#         else:
#             a_line[widx] = input_list[lidx]
#             lidx += 1
# 
#     triangle.append(a_line)

triangle = []
for _ in range(n):
    triangle.append(list(map(int, input().split())))
    
# 0 1 2 3 
# 0 1 2 3 4
# 
# 0 -> 0
# 1 -> 0, 1
# 2 -> 1, 2
# 3 -> 2, 3
# 4 -> 3
sum = [triangle[0]]
for lidx in range(1, n):
    temp_line = []
    for tlidx, titem in enumerate(triangle[lidx]):
        prev_line = sum[lidx-1]
        if tlidx == 0:
            right_prev = prev_line[tlidx]
            temp_line.append(titem + right_prev)
        elif tlidx == len(triangle[lidx])-1:
            left_prev = prev_line[tlidx]
            temp_line.append(titem + left_prev)
        else:
            left_prev = prev_line[tlidx-1]
            right_prev = prev_line[tlidx]
            
            temp_line.append(titem + left_prev)
            temp_line.append(titem + right_prev)
    sum.append(temp_line)