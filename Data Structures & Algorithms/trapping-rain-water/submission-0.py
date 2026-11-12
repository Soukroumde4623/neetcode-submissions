class Solution:
    def trap(self, height: List[int]) -> int:
        left = 1
        right = len(height)-2
        lmax = height[0]
        rmax= height[len(height)-1]
        res=0

        if not height:
            return res
      
        while left<=right:

            if rmax>=lmax:
               res+= max(0, lmax-height[left])
               lmax = max(lmax, height[left])
               left+=1
            
            else:
               res+= max(0, rmax-height[right])
               rmax= max(rmax, height[right])
               right-=1

        return res
        