class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        result = []
        
        for number in range(1, n+1):
            #check if the number is divisible by 3 or 5
            
            is_divisible_by_3 = ((number % 3) == 0);
            is_divisible_by_5 = ((number % 5) == 0)
            #if the number is divided by 3 and 5
            if(is_divisible_by_3 and is_divisible_by_5):
                result.append("FizzBuzz")
            #if the number is divided by 3 only
            elif(is_divisible_by_3):
                result.append("Fizz")
            #if the number is divided by 5 only
            elif (is_divisible_by_5):
                result.append("Buzz")
            #if the number can not be divided byt both 3 and 5
            else:
                result.append(str(number))
                
        return result
