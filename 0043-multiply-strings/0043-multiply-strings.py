class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        nu1 = nu2 = 0
        ten = 1
        for i in range(1, len(num1) + 1):
            nu1 += ten * int(num1[-i])
            ten *= 10
        ten = 1
        for j in range(1,len(num2) + 1):
            nu2 += ten * int(num2[-j])
            ten *= 10
        return str(nu1 * nu2)