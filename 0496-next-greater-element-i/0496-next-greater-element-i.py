class Solution:
    def nextGreaterElement(self, nums1, nums2):
        output = [0]
        nge = [-1] * len(nums2)
        mapper = {}
        for i in range(len(nums2)):
            mapper[nums2[i]] = i
            while (len(output)!=0) and nums2[output[-1]] < nums2[i]:
                nge[output[-1]] = nums2[i]
                output.pop()
            output.append(i)
        output = []
        for i in nums1:
            output.append(nge[mapper[i]])
        return output