# Exercise 6: Recursion

# Calculate factorial recursively
def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)

# Reverse a string recursively
def reverse_string(s):
    if len(s) <= 1:
        return s
    return reverse_string(s[1:]) + s[0]

# Sum a list recursively
def sum_list(lst):
    if not lst:
        return 0
    return lst[0] + sum_list(lst[1:])

# Implement binary search recursively
def binary_search(arr, target, low=0, high=None):
    if high is None:
        high = len(arr) - 1
    if low > high:
        return -1
    mid = (low + high) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] > target:
        return binary_search(arr, target, low, mid - 1)
    else:
        return binary_search(arr, target, mid + 1, high)

# Flatten a nested list recursively
def flatten_list(nested):
    result = []
    for item in nested:
        if isinstance(item, list):
            result.extend(flatten_list(item))
        else:
            result.append(item)
    return result

# Test code
print("Factorial 5:", factorial(5))  # 120
print("Reverse 'hello':", reverse_string("hello"))  # olleh
print("Sum [1,2,3,4,5]:", sum_list([1, 2, 3, 4, 5]))  # 15
print("Binary search [1,3,5,7,9] for 5:", binary_search([1, 3, 5, 7, 9], 5))  # 2
print("Flatten [[1,2],[3,[4,5]]]:", flatten_list([[1, 2], [3, [4, 5]]]))  # [1, 2, 3, 4, 5]
