class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = [1] * (len(nums)) # Initialize answer array with 1s

        # Calculate prefix products first
        for i in range(1, len(nums)): 
            answer[i] = answer[i-1] * nums[i-1]
        
        postfix = 1  # Initialize postfix variable for calculating suffix products

         # Calculate suffix products and update answer array simultaneously
        for i in range(len(nums) -1, -1, -1):
            answer[i] *= postfix # Multiply the current element in the answer array by the postfix value (suffix product)
            postfix *= nums[i] # Update postfix for the next iteration by multiplying it with the current element in nums

        return answer

# in order to solve this problem, we had to look at prefix and post fix
# of the index except it self.
# using nums = [1,2,3,4]
# Initialize the answer array with 1s:
# answer = [1, 1, 1, 1]

# Calculate prefix products:

# For i = 1, answer[1] = answer[0] * nums[0] = 1 * 1 = 1
# For i = 2, answer[2] = answer[1] * nums[1] = 1 * 2 = 2
# For i = 3, answer[3] = answer[2] * nums[2] = 2 * 3 = 6
# So, after prefix products, answer = [1, 1, 2, 6]

# Initialize postfix variable to 1.

# Calculate postfix products and update answer array simultaneously:

# For i = 3 (last element), answer[3] *= postfix = 6 * 1 = 6, postfix *= nums[3] = 1 * 4 = 4
# For i = 2, answer[2] *= postfix = 2 * 4 = 8, postfix *= nums[2] = 4 * 3 = 12
# For i = 1, answer[1] *= postfix = 1 * 12 = 12, postfix *= nums[1] = 12 * 2 = 24
# For i = 0 (first element), answer[0] *= postfix = 1 * 24 = 24, postfix *= nums[0] = 24 * 1 = 24
# So, after postfix products, answer = [24, 12, 8, 6]
# Therefore, the final answer array is [24, 12, 8, 6], which represents the product of all elements except self for each element in the input array [1, 2, 3, 4].