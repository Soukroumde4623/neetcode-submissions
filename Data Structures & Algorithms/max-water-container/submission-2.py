class Solution:
    def maxArea(self, heights: List[int]) -> int:
        if len(heights)==0:
            return 0
            
        maxArea =0
        i = 0
        j = len(heights)-1
     
        while i<j:
            maxArea = max(maxArea,(j-i)*min(heights[j], heights[i]))
            if heights[j]>heights[i]:
                i+=1
            else:    
                j-=1
        return maxArea