class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m=len(matrix)
        n=len(matrix[0])
        
        left=0
        right=m-1
        i=0

        while left<=right:
            mid=left+(right-left)//2

            if target==matrix[mid][n-1]:
                return True
            elif target<=matrix[mid][n-1]:
                i=mid
                right=mid-1
            else:
                left=mid+1
        
        left=0
        right=n-1
        j=0

        while left<=right:
            mid=left+(right-left)//2

            if target==matrix[i][mid]:
                return True
            elif target<=matrix[i][mid]:
                j=mid
                right=mid-1
            else:
                left=mid+1
        
        return False