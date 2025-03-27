# Quick Sort Algorithm
arr = list(map(int, input("Enter numbers separated by space: ").split()))  # User input

# Quick Sort without function (step by step)
if len(arr) > 1:
    pivot = arr[len(arr) // 2]  # Choosing middle element as pivot

    # Creating left list (elements smaller than pivot)
    left = []
    for x in arr:
        if x < pivot:
            left.append(x)

    # Creating middle list (elements equal to pivot)
    middle = []
    for x in arr:
        if x == pivot:
            middle.append(x)

    # Creating right list (elements greater than pivot)
    right = []
    for x in arr:
        if x > pivot:
            right.append(x)

    # Sorting manually using sorted()
    sorted_arr = sorted(left) + middle + sorted(right)
else:
    sorted_arr = arr  # If 1 or 0 elements, it's already sorted

print("Sorted array:", sorted_arr)


# Example 1:
# Input: N = 6, array[] = {13,46,24,52,20,9}
# Output: 9,13,20,24,46,52
# Explanation: After sorting the array is: 9, 13, 20, 24, 46, 52

# Example 2:
# Input: N=5, array[] = {5,4,3,2,1}
# Output: 1,2,3,4,5
# Explanation: After sorting the array is: 1, 2, 3, 4, 5