class Tri:
    def __init__(self):
        # Fill array with 38 zeros
        n = 38
        self.nums = nums = [0] * n
        
        # Address base values
        nums[1] = nums[2] = 1
        for i in range(3, n):
            nums[i] = nums[i - 1] + nums[i - 2] + nums[i - 3]
                    
class Solution:
    t = Tri()
    def tribonacci(self, n: int) -> int:
        return self.t.nums[n]
