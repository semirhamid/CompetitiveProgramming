class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        m=len(mat)
        n=len(mat[0])
        prefMat=[[0 for i in range(n)] for j in range(m)]
        for i in range(m):
            prefMat[i][0]= mat[i][0]
            for j in range(1,n):
                prefMat[i][j]=prefMat[i][j-1]+mat[i][j]  
                
        for i in range(n):
            prefMat[0][i]=prefMat[0][i]
            for j in range(1,m):
                prefMat[j][i]=prefMat[j-1][i]+prefMat[j][i]
        
        
        for i in range(m):
            ru=max(i-k,0)
            rd=min(i+k,m-1)
            for j in range(n):
                cl=max(0,j-k)
                cr=min(n-1,j+k)
                value=prefMat[rd][cr]
                if ru-1>=0:
                    value-=prefMat[ru-1][cr]
                if cl-1>=0:
                    value-=prefMat[rd][cl-1]
                if ru-1>=0 and cl-1>=0:
                    value+=prefMat[ru-1][cl-1]
                
                mat[i][j]=value
        return mat