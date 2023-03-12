def two_sums(nums, target):
    # Base case

    # Main code case
    # temp = nums.copy()
    # for ind in range(len(nums)):
    #     current = temp.pop(0)
    #     if (target - current) in temp:
    #         return [ind, nums.index(target - current)]

    check = {}
    for ind, num in enumerate(nums):
        if (target - num) in check:
            return [check[(target - num)], ind]
        elif (target - num) not in check:
            check[num] = ind


def main():
    # Inputs and expected outputs
    inputs = (([2, 7, 11, 15], 9), ([3, 2, 4], 6), ([3, 3], 6))
    expected_output = ([0, 1], [1, 2], [0, 1])

    
    # Cycle through each input and print result of my function vs expected output
    for ind, input in enumerate(inputs):
        result = two_sums(input[0], input[1])
        print(result, expected_output[ind])

if __name__ == "__main__":
    main()