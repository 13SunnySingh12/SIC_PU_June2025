def calculate_minimum_total_cost(num_buyers, flower_costs):

    flower_costs.sort(reverse=True)
    total_cost = 0

    # Loop through each flower and assign a multiplier based on buyer's turn
    for index, cost in enumerate(flower_costs):
        purchase_round = index // num_buyers
        total_cost += (purchase_round + 1) * cost

    return total_cost

if __name__ == '__main__':

    num_flowers, num_buyers = map(int, input().strip().split())

    flower_costs = list(map(int, input().strip().split()))

    minimum_total_cost = calculate_minimum_total_cost(num_buyers, flower_costs)
    print(minimum_total_cost)
