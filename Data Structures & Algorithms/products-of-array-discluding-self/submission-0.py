class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [0]*len(nums)
        suffix = [0]*len(nums)
        
        prefix[0]=1
        suffix[len(suffix)-1]=1
        pred1=1
        pred2=1

        for i in range(1,len(nums)):
             pred1 =pred1*nums[i-1]
             prefix[i] = pred1

        for i in range(len(nums)-2, -1, -1):
            pred2 = pred2*nums[i+1]
            suffix[i] = pred2

        results = []
        for j in range(0,len(nums)):
             results.append(suffix[j]*prefix[j])

        return results


