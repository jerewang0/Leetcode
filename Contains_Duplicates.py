def containDuplicate(nums):
    # Base case
    if len(nums) == 0:
        return False

    # Main code case
    count = {}
    for num in nums:
        if num not in count:
            count[num] = 1
        else:
            count[num] += 1
            return True
    return False

def main():
    # Inputs and expected outputs
    inputs = ([1, 2, 3, 1], [1, 2, 3, 4], [1, 1, 1, 3, 3, 4, 3, 2, 4, 2])
    expected_output = [True, False, True]
    print(inputs)
    
    # Cycle through each input and print result of my function vs expected output
    for ind, arr in enumerate(inputs):
        result = containDuplicate(arr)
        print(result, expected_output[ind])

if __name__ == "__main__":
    main()