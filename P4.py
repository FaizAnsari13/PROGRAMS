def first_non_repeated_character(input_str):
    char_count = {}  # Dictionary to store character counts

    # Count occurrences of each character in the string
    for char in input_str:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    # Find the first non-repeated character
    for char in input_str:
        if char_count[char] == 1:
            return char

    return None  # If no non-repeated character is found

# Example usage:
input_string = "abacddce"
result = first_non_repeated_character(input_string)

if result:
    print(f"The first non-repeated character is: {result}")
else:
    print("No non-repeated character found.")
