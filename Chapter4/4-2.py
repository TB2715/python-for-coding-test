from tqdm import tqdm


def self_solution():
    n = int(input())

    count = 0
    for i in tqdm(range(n+1), desc='hours'):
        for min in range(60):
            for sec in range(60):
                # time = list(str(i) + str(min) + str(sec))

                if '3' in str(i) + str(min) + str(sec):
                    count += 1

    print(count)


if __name__ == '__main__':
    self_solution()