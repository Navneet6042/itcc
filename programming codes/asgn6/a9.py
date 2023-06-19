class ParenthesesValidator:
    def __init__(self):
        self.opening_brackets = ['(', '{', '[']
        self.closing_brackets = [')', '}', ']']

    def is_valid(self, parentheses_string):
        stack = []

        for char in parentheses_string:
            if char in self.opening_brackets:
                stack.append(char)
            elif char in self.closing_brackets:
                if not stack or self.opening_brackets.index(stack.pop()) != self.closing_brackets.index(char):
                    return False

        return len(stack) == 0


# Usage Example:
validator = ParenthesesValidator()

# Test with valid strings
print(validator.is_valid("()"))        # True
print(validator.is_valid("(DI"))       # False
print(validator.is_valid("{I}"))       # True
print(validator.is_valid("[0110]"))    # True

# Test with invalid strings
print(validator.is_valid(")("))        # False
print(validator.is_valid("{"))         # False
print(validator.is_valid("}"))         # False
print(validator.is_valid("[[[]]"))     # False
