import bisect
def solver(costs, money):
    costs.sort()
    if money >= min(costs):
        index = bisect.bisect(costs,money)
        return len(costs[0:index])
    else:
        return 0


if __name__ == '__main__':
    np = input()
    st = input()
    cash = []
    costs = list(map(int,st.split()))
    y = input()
    while y:
        y = int(input())
        if not y:
            break
        print(solver(costs,y))
