def isAnagram(s, t):
    # Base case
    if len(s) == 0 or len(t) == 0:
        return False

    # Main code case
    count = {}
    for letter in s:
        if letter not in count:
            count[letter] = 1
        else:
            count[letter] += 1

    for new_letter in t:
        if new_letter in count:
            count[new_letter] -= 1
            if count[new_letter] < 0:
                return False
        else:
            return False
    return True
    

def main():
    # Inputs and expected outputs
    inputs = (("anagram", "nagaram"), ("rat", "car"))
    expected_output = (True, False)
    
    # Cycle through each input and print result of my function vs expected output
    for ind, input in enumerate(inputs):
        result = isAnagram(input[0], input[1])
        print(result, expected_output[ind])

if __name__ == "__main__":
    main()