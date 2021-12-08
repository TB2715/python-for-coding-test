a, b, v = map(int, input().split())

expect = (v-b)//(a-b)
if (v-b)%(a-b) > 0:
    print(expect + 1)
else:
    print(expect)