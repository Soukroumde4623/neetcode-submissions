class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = []

        for i, current_temp in enumerate(temperatures):
            while stack and current_temp>temperatures[stack[-1]]:
                index = stack.pop()
                result[index] = i -index
            stack.append(i)
        
        return result
             


        