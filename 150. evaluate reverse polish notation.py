# 150. Evaluate reverse polish notation
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        for letter in tokens:
            if letter == "+":
                stack.append(stack.pop() + stack.pop())
            elif letter == "-":
                num1 = stack.pop()
                num2 = stack.pop()
                stack.append(num2 - num1)
            elif letter == "*":
                stack.append(stack.pop() * stack.pop())
            elif letter == "/":
                num1 = stack.pop()
                num2 = stack.pop()
                stack.append(int(num2 / num1))
            else:
                stack.append(int(letter))
        return stack[0]