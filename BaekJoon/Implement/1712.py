a_cost, b_cost, c_price = map(int, input().split())

if c_price <= b_cost:
    print(-1)

else:
    count = (a_cost // (c_price - b_cost)) + 1
    print(count)
