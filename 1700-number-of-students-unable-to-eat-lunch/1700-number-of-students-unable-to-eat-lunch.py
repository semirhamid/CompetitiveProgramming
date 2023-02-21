class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        stud = dict(Counter(students))
        for i in sandwiches:
            if stud.get(i, False) and stud[i] > 0:
                stud[i] -= 1
            else:
                count = 0
                for i in stud:
                    count += stud[i]
                return count
        return 0