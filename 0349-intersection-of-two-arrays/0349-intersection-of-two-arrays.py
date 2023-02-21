class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()
        result = {}
        i = j = 0
        lennum1 = len(nums1)
        lennum2 = len(nums2)
        while i < lennum1 and j < lennum2:
            if nums1[i] > nums2[j]:
                j += 1
            elif nums1[i]<nums2[j]:
                i += 1
            else:
                if nums1[i] not in result and nums1[i] == nums2[j]:
                    result[nums1[i]] = 1
                i += 1
                j += 1
        return list(result)