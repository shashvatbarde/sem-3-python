# Bottom-Up Approach
def knapsack_bottom_up(values, weights, W):
    n = len(values)
    # Create a table with n+1 rows and W+1 columns
    dp = [[0 for _ in range(W + 1)] for _ in range(n + 1)]
    # Fill the table
    for i in range(1, n + 1):
        for w in range(W + 1):
            # If current item can fit
            if weights[i - 1] <= w:
                # Choose maximum of:
                # 1. Not taking the item
                # 2. Taking the item
                dp[i][w] = max(
                    dp[i - 1][w],
                    dp[i - 1][w - weights[i - 1]] + values[i - 1]
                )
            else:
                # Item cannot fit
                dp[i][w] = dp[i - 1][w]
    return dp[n][W]
# Top-Down Approach
def knapsack_top_down(values, weights, W):
    n = len(values)
    # Create a table to store already calculated results
    dp = [[-1 for _ in range(W + 1)] for _ in range(n + 1)]
    def solve(i, w):
        # Base condition
        if i == 0 or w == 0:
            return 0
        # If result is already calculated
        if dp[i][w] != -1:
            return dp[i][w]
        # If item can fit
        if weights[i - 1] <= w:
            dp[i][w] = max(
                solve(i - 1, w),
                solve(i - 1, w - weights[i - 1]) + values[i - 1]
            )
        else:
            dp[i][w] = solve(i - 1, w)
        return dp[i][w]
    return solve(n, W)
# Main Program
print("0/1 Knapsack Problem")
# Taking input from user
n = int(input("Enter number of items: "))
values = []
weights = []
for i in range(n):
    value = int(input("Enter value of item " + str(i + 1) + ": "))
    weight = int(input("Enter weight of item " + str(i + 1) + ": "))
    values.append(value)
    weights.append(weight)
W = int(input("Enter maximum weight capacity: "))
print("\nValues:", values)
print("Weights:", weights)
print("Capacity:", W)
# Bottom-Up result
result1 = knapsack_bottom_up(values, weights, W)
# Top-Down result
result2 = knapsack_top_down(values, weights, W)
print("\nBottom-Up Maximum Value:", result1)
print("Top-Down Maximum Value:", result2)
