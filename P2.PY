def reverse_array_in_place(arr):
    start = 0
    end = len(arr) - 1

    while start < end:
        # Swap elements at start and end positions
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1

# Example usage:
my_array = [1, 2, 3, 4, 5]
reverse_array_in_place(my_array)
print(my_array)
