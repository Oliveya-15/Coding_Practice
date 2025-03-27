# Merge Sort Algorithm
n = int(input("Enter the number of elements: "))  # Take the number of inputs
arr = list(map(int, input("Enter the numbers separated by space: ").split()))  # Take array input

# Ensure the user enters the correct number of elements
if len(arr) != n:
    print("Error: You must enter exactly", n, "numbers.")
else:
    # Sorting process
    if len(arr) > 1:
        mid = len(arr) // 2  # Find the middle index

        # Splitting the array into two halves
        left = arr[:mid]   # Left half
        right = arr[mid:]  # Right half

        # Sorting each half separately
        left = sorted(left)
        right = sorted(right)

        # Merging the sorted halves
        sorted_arr = []
        i = j = 0  # Pointers for left and right arrays

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                sorted_arr.append(left[i])
                i += 1
            else:
                sorted_arr.append(right[j])
                j += 1

        # Add remaining elements from left (if any)
        while i < len(left):
            sorted_arr.append(left[i])
            i += 1

        # Add remaining elements from right (if any)
        while j < len(right):
            sorted_arr.append(right[j])
            j += 1
    else:
        sorted_arr = arr  # If 1 or 0 elements, already sorted

    print("Sorted array:", sorted_arr)


# Example 1:
# Input: N = 6, array[] = {13,46,24,52,20,9}
# Output: 9,13,20,24,46,52
# Explanation: After sorting the array is: 9, 13, 20, 24, 46, 52

# Example 2:
# Input: N=5, array[] = {5,4,3,2,1}
# Output: 1,2,3,4,5
# Explanation: After sorting the array is: 1, 2, 3, 4, 5
