class Solution(object):
    def plusOne(self, digits):
        # Adjusting an array of digits into an integer
        digits_integer = int(''.join(map(str,digits)))
        digits_integer +=1
        # Adjusting back an integer into an array of digits after plus 1
        return [int(x) for x in str(digits_integer)]