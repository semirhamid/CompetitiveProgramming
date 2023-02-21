class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        st = set()
        for i in nums:
            st.add(i)
            temp = str(i)
            st.add(int(temp[::-1]))
        return len(st)