class Solution:
    # To find the length of the longest consecutive elements sequence in an unsorted array of integers nums, we can use a HashSet to store all the elements in nums. Then, for each element num in nums, we can check if num - 1 is in the HashSet. 
    # If not, num could potentially be the start of a consecutive sequence. We can then count the length of the consecutive sequence starting from num. We update the maximum length of consecutive sequences found as we iterate through nums.
    def longestConsecutive(self, nums: List[int]) -> int:
        # hashset = set(nums) # intializing nums as hashset
        # longest_sequence = 0 # initalizing variable

        # for i in nums: # iterating through nums 
        #     if (i-1) not in hashset: # checking to see if there is a value to left of that is sequenced i = 99, checking to see if there is 98
        #         length = 0 # initialzing length to capture most consecutive sequence
        #         while (i + length) in hashset: # if there is a sequence, loop it to add them all up
        #             length += 1  # adding the highest length
                
        #         longest_sequence = max(length, longest_sequence) # getting the max sequence and adjusting it
        
        # return longest_sequence

## another method
        # Convert nums to a set for O(1) lookup
        num_set = set(nums)
        max_length = 0

        # Iterate through each element in nums
        for num in num_set:
            # Check if num - 1 is in the set
            if num - 1 not in num_set:
                current_num = num
                current_length = 1

                # Check if consecutive numbers starting from current_num exist in the set
                while current_num + 1 in num_set:
                    current_num += 1
                    current_length += 1

                # Update the maximum length found
                max_length = max(max_length, current_length)

        return max_length