class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        left = 0
        right = 0
        temp = nums1.copy()
        i = 0
        while right < n and left < m:
            if temp[left] < nums2[right]:
                nums1[i] = temp[left]
                left += 1
            else:
                nums1[i] = nums2[right]
                right += 1
            i += 1

        for right in range(right, n):
            nums1[i] = nums2[right]

            i += 1
        for left in range(left, m):
            nums1[i] = temp[left]
            i += 1