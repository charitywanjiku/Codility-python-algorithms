

def digit_sum(num):
    return sum(int(digit) for digit in str(num))

def solution(A):
    max_sum = -1
    
    # Dictionary to store numbers based on their digit sums
    num_dict = {}
    
    # Iterate through the array
    for num in A:
        # Calculate digit sum of the current number
        sum_digits = digit_sum(num)
        
        # Check if there is a number with the same digit sum in the dictionary
        if sum_digits in num_dict:
            # Update max_sum if the sum of current number and the number in the dictionary is greater
            max_sum = max(max_sum, num + num_dict[sum_digits])
        
        # Add current number to the dictionary
        num_dict[sum_digits] = max(num, num_dict.get(sum_digits, -1))
    
    return max_sum

# Test cases
print(solution([51,71,17,42])) # Output: 93
print(solution([42,33,60]))    # Output: 102
print(solution([51,32,43]))    #Output:  -1