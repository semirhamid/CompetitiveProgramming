class Solution(object):
    def evalRPN(self, tokens):
        numbers = []
        for i in tokens:
            if i not in "+-*/":
                numbers.append(int(i))
            else:
                right = numbers.pop()
                left = numbers.pop()
                if i == "+":
                    numbers.append(left+right)
                elif i == "-":
                    numbers.append(left-right)
                elif i == "*":
                    numbers.append(left*right)
                else:
                    numbers.append(int(float(left)/right))
        return numbers.pop()