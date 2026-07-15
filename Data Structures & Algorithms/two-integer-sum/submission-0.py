class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # stores [num,index]
        seen = {}
        
        # iterate nums
        for i,num in enumerate(nums):
            diff = target - num
            # num not seen, add to seen with its index
            if diff in seen:
                return [seen[diff],i]
            seen[num] = i