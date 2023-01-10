class Solution:
    def interpret(self, command: str) -> str:
        left = 0
        result = ""
        while left < len(command):
            if command[left] != "(":
                result += "G"
                left += 1
            elif command[left] + command[left + 1] == "()":
                result += "o"
                left += 2
            else:
                result += "al"
                left += 4

        return result