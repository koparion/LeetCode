class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashset = set() #to store values in the hash into set
        for count in nums:
            if count in hashset:
                return True

            hashset.add(count) #adding value to hashset when there is no duplicate
        return False # returning false when there is no duplicates in the whole array