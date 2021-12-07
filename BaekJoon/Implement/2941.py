def self_solution():
    croa_list = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
    croa_dict = {
        'c' : {
            'c=': None,
            'c-': None
        },
        'd' : {
            'dz':{
                'dz=': None,
            },
            'd-': None
        },
        'l': {'lj': None},
        'n': {'nj': None},
        's': {'s=': None},
        'z': {'z=': None},
    }


    user_input = input()
    temp_dict = croa_dict
    temp_char = user_input[0]
    count = 0

    for ua_idx in range(1, len(user_input)):
        if temp_char in temp_dict.keys():
            if temp_dict[temp_char] == None:
                pass
            else:
                temp_dict = temp_dict[temp_char]
                temp_char += user_input[ua_idx]
                continue

        temp_dict = croa_dict
        temp_char = user_input[ua_idx]
        count += 1

    if temp_char in temp_dict.keys() and temp_dict[temp_char] is None:
        count += 1
    else:
        count += len(temp_char)

    print(count)


def solution():
    croa_list = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
    user_input = input()

    for croa in croa_list:
        user_input = user_input.replace(croa, '*')

    print(len(user_input))


if __name__ == '__main__':
    solution()