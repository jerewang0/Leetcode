def isPalindrome(x):
    # Base case
    if len(x) <= 1:
        return False

    # Main code case
    conv_to_str = str(x)

    for ind in range(len(conv_to_str)//2):
        if conv_to_str[ind] != conv_to_str[-(ind + 1)]:
            return False
    return True


def main():
    # Inputs and expected outputs
    inputs = (121, -121, 10)
    expected_output = (True, False, False)

    
    # Cycle through each input and print result of my function vs expected output
    for ind, input in enumerate(inputs):
        result = isPalindrome(input)
        print(result, expected_output[ind])

if __name__ == "__main__":
    main()