def can_be_arranged(n, boys, girls):
    boys.sort()
    girls.sort()

    def is_valid(arrangement):
        for i in range(1, len(arrangement)):
            if (arrangement[i] < arrangement[i - 1]):
                return False
        return True


    boy_girl_order = []
    for i in range(n):
        boy_girl_order.append(boys[i])
        boy_girl_order.append(girls[i])

    if (is_valid(boy_girl_order)):
        return "YES"
    else:

        girl_boy_order = []
        for i in range(n):
            girl_boy_order.append(girls[i])
            girl_boy_order.append(boys[i])

        if (is_valid(girl_boy_order)):
            return "YES"
        else:
            return "NO"

# Input handling
t = int(input())

for test_case in range(t):
    n = int(input())
    boys = list(map(int, input().split()))
    girls = list(map(int, input().split()))

    result = can_be_arranged(n, boys, girls)
    print(result)
