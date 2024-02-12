class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # hashmap = {}

        # for i, value in enumerate(nums): #adding counter using enumerate
        #     remaining = target - nums[i]

        #     if remaining in hashmap:
        #         return[i, hashmap[remaining]]
        #     else:
        #         hashmap[value] = i
         # Iterate through the indices of nums

        ## another way
        # hashmap = {}
        # for i in range(len(nums)):
        #     value = nums[i]
        #     sum = target - value

        #     # Check if the remaining value exists in hashmap
        #     if sum in hashmap:
        #         # If yes, return the indices of the current element and the index of its complement
        #         return [hashmap[sum], i]
        #     else:
        #         # If not, add the current value and its index to hashmap
        #         hashmap[value] = i

        ## 3rd way
        seen = set()

        for i in range(len(nums)):
            complement = target - nums[i]

            if complement in seen:
                # If the complement is in the set, return its index and the current index
                return [nums.index(complement), i]
            else:
                # Otherwise, add the current number and its index to the set
                seen.add(nums[i])