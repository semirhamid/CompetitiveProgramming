class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        left = 0
        right = len(arr) - 1
        if len(arr) < 3: return False
        flag = True
        while left  < right :
            if(arr[left] < arr[left + 1]):
                left += 1
                continue
            
            else:
                
                if left == 0:
                    return False
                else:
                    flag = False
                    while left < right:
                        if arr[left] <= arr[left + 1]:
                            return False
                        left += 1
            
        if flag : return False
        return True
            