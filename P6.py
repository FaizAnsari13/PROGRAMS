def postfix_to_prefix(postfix_expression):
    stack = []
    
    operators = set(['+', '-', '*', '/', '^'])
    
    for token in postfix_expression:
        if token not in operators:
            stack.append(token)
        else:
            operand1 = stack.pop()
            operand2 = stack.pop()
            prefix_expression = token + operand2 + operand1
            stack.append(prefix_expression)
    
    return stack[0]

# Example usage:
postfix_expression = "ab+cd-*"
prefix_expression = postfix_to_prefix(postfix_expression)
print(f"Postfix: {postfix_expression}")
print(f"Prefix: {prefix_expression}")
