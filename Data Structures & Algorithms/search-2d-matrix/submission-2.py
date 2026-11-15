class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
         i=0
         while i<len(matrix) and target>matrix[i][-1]:
               i+=1
         
         if i == len(matrix):
             return False

         debut=0
         fin = len(matrix[i])-1

         while debut <= fin :

            mid = (debut+fin)//2
            if target == matrix[i][mid]:
                 return True 
            elif target<matrix[i][mid]:
                 fin = mid-1
            else:
                debut= mid+1
         return False