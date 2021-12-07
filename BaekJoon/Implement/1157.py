user_input = input()

a_index = ord('a')
z_index = ord('z')

alpha_dict = {chr(k): 0 for k in range(a_index, z_index+1)}

for char in user_input:
    alpha_dict[char.lower()] += 1

sorted_dict = sorted(alpha_dict.items(), key=lambda x: x[1], reverse=True)

top = sorted_dict[0][1]
second = sorted_dict[1][1]

if top == second:
    print('?')
else:
    print((sorted_dict[0][0]).upper())