class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # initiation:
        memory = {}

        # iterate the list
        for num in nums:
            if num in memory: # checking if a key (i.e. nums) is int he dictionary
                return True
            else:
                memory[num] = 1
        
        return False
