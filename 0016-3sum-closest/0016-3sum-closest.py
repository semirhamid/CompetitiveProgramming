class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        closest = math.inf
        res = 0
        
        for ptr1 in range(len(nums)-2):
            cur_target = target - nums[ptr1]
            ptr2, ptr3 = ptr1+1, len(nums)-1
            while ptr3 - ptr2 > 0:
                s = nums[ptr2] + nums[ptr3]
                if abs(cur_target - s) < closest:
                    closest = abs(cur_target - s)
                    res = s + nums[ptr1]
                if cur_target < s:
                    ptr3 -= 1
                elif cur_target > s:
                    ptr2 += 1
                else:
                    # found the closest sum possible; target itself
                    return target
                
        return res