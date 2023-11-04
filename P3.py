def are_strings_rotations(str1, str2):
    if len(str1) != len(str2):
        return False

    concatenated_str = str1 + str1
    if str2 in concatenated_str:
        return True
    else:
        return False

# Example usage:
string1 = "abcdef"
string2 = "defabc"
if are_strings_rotations(string1, string2):
    print(f"{string1} and {string2} are rotations of each other.")
else:
    print(f"{string1} and {string2} are not rotations of each other.")
