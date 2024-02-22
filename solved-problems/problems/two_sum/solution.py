class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}  # Initialize a hashmap to store numbers and their indices

        # Iterate through the indices of the input list 'nums'
        for i in range(len(nums)):
            difference = target - nums[i]  # Calculate the difference between the target and the current number
            
            # Check if the difference exists in the hashmap
            if difference in hashmap:
                return [hashmap[difference], i]  # If found, return the indices of the difference and the current number
            
            hashmap[nums[i]] = i  # Store the current number and its index in the hashmap

        return []  # Return an empty list if no solution is found
