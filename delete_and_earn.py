class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        points = defaultdict(int)
        max_number = 0
        
        for num in nums:
            points[num] += num
            max_number = max(max_number, num)
            
        @cache
        def max_points(number):
            if number == 0:
                return 0
            if number == 1:
                return points[1]
            
            return max(max_points(number - 1), max_points(number - 2) + points[number])
        
        return max_points(max_number)
