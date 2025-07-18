test_cases = int(input())

for _ in range(test_cases):
    N, current_player = map(int, input().split())

    history = [current_player]y

    for _ in range(N):
        command = input().strip()

        if command == "B":
            history.pop()
        else:
            _, new_player = command.split()
            history.append(int(new_player))

    print("Player", history[-1])
