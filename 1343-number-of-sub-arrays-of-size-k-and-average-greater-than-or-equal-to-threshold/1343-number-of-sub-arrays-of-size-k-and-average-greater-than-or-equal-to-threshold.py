class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        temp = sum(arr[:k])
        count =  1 if temp/k >= threshold else 0
        for right in range(k,len(arr)):
            temp += arr[right]
            temp -= arr[right - k]
            if temp/k >= threshold:
                count += 1

        return count