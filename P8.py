def are_brackets_properly_closed(code_snippet):
    stack = []
    opening_brackets = "({["
    closing_brackets = ")}]"
    bracket_pairs = {')': '(', '}': '{', ']': '['}
    
    for char in code_snippet:
        if char in opening_brackets:
            stack.append(char)
        elif char in closing_brackets:
            if not stack or stack.pop() != bracket_pairs[char]:
                return False
    
    return not stack
# Example usage:
code_snippet = "if (x > 0) { print('Hello'); }"
if are_brackets_properly_closed(code_snippet):
    print("Brackets are properly closed.")
else:
    print("Brackets are not properly closed.")
