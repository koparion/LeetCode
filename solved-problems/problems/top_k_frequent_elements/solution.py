class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Create an empty dictionary to store the count of each number
        counter = {}

        # Create a list of lists (buckets) to store numbers based on their frequency
        # Each index of the list corresponds to the frequency of numbers
        # Initialize the list with empty lists
        freq = [[] for i in range(len(nums) + 1)]

        # Count the frequency of each number in nums and store it in the count dictionary
        for i in nums:
            counter[i] = 1 + counter.get(i, 0)

        # Iterate through the items in the count dictionary
        # Each item represents a number and its frequency
        for  number, frequency in counter.items():
            freq[frequency].append(number) # Append the number to the appropriate frequency bucket in the freq list

        res = [] # Initialize an empty list to store the k most frequent elements

        # Iterate through the frequency buckets in reverse order
        # Starting from the highest frequency
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]: # Iterate through the numbers in the current frequency bucke
                res.append(n) # Append the number to the result list

                if len(res) == k:  # Check if we have found k most frequent elements
                    return res # If yes, return the result list

        ## another method
        ## Count the frequency of each element in nums
        #count = Counter(nums)
        
        ## Use heapq's nlargest function to get the k most frequent elements
        #return heapq.nlargest(k, count.keys(), key=count.get)