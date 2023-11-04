def is_operator(char):
    return char in "+-*/^"

def prefix_to_infix(prefix_expression):
    stack = []
    
    # Reverse the prefix expression to process it from right to left
    prefix_expression = prefix_expression[::-1]
    
    for char in prefix_expression:
        if not is_operator(char):
            stack.append(char)
        else:
            operand1 = stack.pop()
            operand2 = stack.pop()
            infix_expression = f"({operand1}{char}{operand2})"
            stack.append(infix_expression)
    
    return stack[0]

# Example usage:
prefix_expression = "*+ab-cd"
infix_expression = prefix_to_infix(prefix_expression)
print(f"Prefix: {prefix_expression}")
print(f"Infix: {infix_expression}")
