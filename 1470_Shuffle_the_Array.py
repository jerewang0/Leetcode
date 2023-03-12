def two_sums(nums, n):
    # Base case

    # Main code case
    result = []

    for i in range(len(nums)//2):
        result += [nums[i], nums[i + n]]
    
    return result


def main():
    # Inputs and expected outputs
    inputs = (([2, 5, 1, 3, 4, 7], 3), ([1, 2, 3, 4, 4, 3, 2, 1], 4), ([1, 1, 2, 2], 2))
    expected_output = ([2, 3, 5, 4, 1, 7], [1, 4, 2, 3, 3, 2, 4, 1], [1, 2, 1, 2])

    
    # Cycle through each input and print result of my function vs expected output
    for ind, input in enumerate(inputs):
        result = two_sums(input[0], input[1])
        print(result, expected_output[ind])

if __name__ == "__main__":
    main()