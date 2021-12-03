def solution():
    city_num = int(input())
    city_distance = input().split()
    city_price = input().split()

    total_price = 0
    current_idx = 0
    current_price = int(city_price[0])
    idx = 1
    while current_idx < city_num-1:
        if int(city_price[idx]) < current_price:
            temp_distance = 0
            for d in city_distance[current_idx:idx]:
                temp_distance += int(d)

            total_price += current_price * temp_distance
            current_idx = idx
            current_price = int(city_price[idx])
            idx += 1
            continue

        else:
            if idx == city_num-1: # 마지막 지역일 경우
                temp_distance = 0
                for d in city_distance[current_idx:idx]:
                    temp_distance += int(d)

                total_price += current_price * temp_distance
                current_idx = idx

            idx += 1

    print(total_price)


if __name__ == '__main__':
    solution()