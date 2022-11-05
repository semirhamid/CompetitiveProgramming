class Solution(object):
    def kthSmallest(self, matrix, k):
        new = []
        for i in matrix:
            for j in i:
                new.append(j)
        new.sort()
        return new[k - 1]