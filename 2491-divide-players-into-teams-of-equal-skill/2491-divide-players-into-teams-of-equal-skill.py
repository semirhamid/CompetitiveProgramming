class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        left = 0
        right = len(skill) - 1
        skill.sort()
        result = []
        while left < right:
            result.append([skill[left],skill[right]])
            left += 1
            right -= 1
        st = set()
        count = 0
        for i in result:
            st.add(i[0] + i[1])
            count += i[0] * i[1]
        
        if len(st) == 1:
            
            return count
        else:
            return -1