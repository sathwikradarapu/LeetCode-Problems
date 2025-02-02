from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        
        for token in tokens:
            if token.isnumeric() or (token.startswith('-') and token[1:].isnumeric()):
                # Handle both positive and negative numbers
                stack.append(int(token))
            else:
                a = stack.pop()  # Second operand
                b = stack.pop()  # First operand
                
                if token == '+':
                    stack.append(b + a)
                elif token == '-':
                    stack.append(b - a)
                elif token == '*':
                    stack.append(b * a)
                elif token == '/':
                    # Ensure truncation towards zero
                    stack.append(int(b / a))
        
        return stack[0]  # Final result will be the only element in stack
