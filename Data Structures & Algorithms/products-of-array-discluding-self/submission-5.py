class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # initiation
        forward = []
        backwards = []
        index = 0

        # iteration
        while index < len(nums):
            # print(f"{index}: {nums[index]}")
            if index == 0:
                forward.append(nums[index]) # index = 0
                backwards.append(nums[index-1]) # index = 0-1 = -1
            else:
                forward.append(nums[index] * forward[index-1]) # index = 1,2,3,4,... ; forward = 0,1,2,3,...
                backwards.append(nums[index*-1 -1] * backwards[index-1]) # index = 1,2,3,4 ; backwards = 
            # print(forward)
            # print(backwards)
            index += 1

        # print("="*20)

        # output
        output = []
        output.append(backwards[-2])
        # print(output)
        index = 1
        while index < len(nums) - 1: # index = 1,2,..., len(nums) - 2
            output.append(forward[index-1] * backwards[len(nums)-index-2]) # backwards is built from the end of nums
            index += 1
            # print(output)

        output.append(forward[-2])
        # print(output)
        return output

        