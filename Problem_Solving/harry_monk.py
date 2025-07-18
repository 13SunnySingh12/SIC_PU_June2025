def monk_and_harry():
    N = int(input())
    harry_coins = list(map(int, input().split()))

    Q, X = map(int, input().split())
    instructions = [input().strip() for _ in range(Q)]

    monk_bag = []             
    monk_bag_value = 0        
    harry_coin_index = 0      

    for instruction in instructions:
        if instruction == "Harry":
            if harry_coin_index < N:
                next_coin = harry_coins[harry_coin_index]
                monk_bag.append(next_coin)
                monk_bag_value += next_coin
                harry_coin_index += 1

        elif instruction == "Remove":
            if monk_bag:
                removed_coin = monk_bag.pop()
                monk_bag_value -= removed_coin

        if monk_bag_value == X:
            print(len(monk_bag))
            return

    print(-1)

monk_and_harry()
