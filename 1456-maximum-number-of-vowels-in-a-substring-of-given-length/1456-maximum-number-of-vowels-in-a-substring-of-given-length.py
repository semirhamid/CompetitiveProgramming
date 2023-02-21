class Solution:
    def maxVowels(self, arr: str, k: int) -> int:
        vowels = "aeiou"
        count = 0
        for i in arr[:k]:
            if i in vowels:
                count += 1
        temp = count
        for right in range(k,len(arr)):
            temp = temp + 1 if(arr[right]) in vowels else temp
            temp = temp - 1 if (arr[right-k]) in vowels else temp
            count = max(count, temp)


        return count
    