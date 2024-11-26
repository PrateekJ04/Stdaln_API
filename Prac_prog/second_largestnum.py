# Find the second largest number in the list without using inbuilt functions


def find_second_largest(numbers):
    # Initialize first and second to a very small value
    first = second = float('-inf')

    # Traverse the list
    for num in numbers:
        if num > first:
            second = first  # previous first becomes second
            first = num  # update first to the current number
        elif num > second and num != first:
            second = num  # update second if it's between first and second

    # If second is still negative infinity, it means no second largest number exists
    return second if second != float('-inf') else None


# Example usage:
numbers = [10, 20, 4, 45, 99]
print("Second largest number is:", find_second_largest(numbers))

