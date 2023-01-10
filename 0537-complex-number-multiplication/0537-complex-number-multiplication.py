class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        real = num1.split("+")
        imaginary = num2.split("+")
        result = ""
        reality = int(real[0]) * int(imaginary[0])
        imagine = int(real[1][:-1]) * int(imaginary[0]) + int(imaginary[1][:-1]) * int(real[0])
        reality += (-1) * (int(real[1][:-1]) * int(imaginary[1][:-1]))
        result += str(reality) + "+" + str(imagine) + "i"
        return result
        