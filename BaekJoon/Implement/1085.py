x, y, w, h = map(int, input().split())

x_right = w-x
y_up = h-y

d_list = x, y, x_right, y_up

print(min(d_list))
