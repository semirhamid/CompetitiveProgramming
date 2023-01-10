class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        longest = 0
        temp = 0
        left = 0
        right = 0
        length = len(arr) -2
        while left < length  and right < length :
            if arr[left] < arr[left + 1]:
                while left < length +1 and arr[left] < arr[left + 1]:
                    left +=1

                temp += (left - right)+1
                right = left
                if right < length+1 and arr[right] > arr[right + 1]:
                    while right < length+1 and  arr[right] > arr[right+1]:
                        right += 1
                diff = right - left
                if diff == 0:
                    temp = 0
                else:
                    temp += diff 
                longest = max(longest, temp)
                left = right
                temp = 0
            else:
                right+=1
                left +=1
        return longest