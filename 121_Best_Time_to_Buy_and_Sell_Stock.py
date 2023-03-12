def maxProfit(prices):
    # Base case
    if len(prices) < 2:
        return 0

    # Main code case
    max_profit = 0
    current = prices[0]
    for ind in range(1, len(prices)):
        if prices[ind] - current > max_profit:
            max_profit = prices[ind] - current
        elif (prices[ind] - current <= max_profit) and current > prices[ind]:
            current = prices[ind]
    return max_profit


def main():
    # Inputs and expected outputs
    inputs = ([7, 1, 5, 3, 6, 4], [7, 6, 4, 3, 1])
    expected_output = (5, 0)

    
    # Cycle through each input and print result of my function vs expected output
    for ind, input in enumerate(inputs):
        result = maxProfit(input)
        print(result, expected_output[ind])

if __name__ == "__main__":
    main()