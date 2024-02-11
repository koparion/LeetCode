class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashmap = {} #creating a hashmap to store string in

        if len(s) != len(t): # checking if lengths match to check for anagram
            return False
        
        for char in s:
            hashmap[char] = hashmap.get(char, 0) + 1 # incrementing counts

        for char in t:
            if char not in hashmap or hashmap[char] == 0:
                return False
            hashmap[char] = hashmap[char] - 1
        
        return all(count == 0 for count in hashmap.values())

# another method using 1 for loop
        # hashmapS = {} #creating a hashmap to store string in
        # hashmapT = {}

        # if len(s) != len(t): # checking if lengths match to check for anagram
        #     return false

        # for i in range(len(s)):
        #      hashmapS[s[i]] = 1 + hashmapS.get(s[i], 0) # counting the times value in string s
        #      hashmapT[t[i]] = 1 + hashmapT.get(t[i], 0) # counting the times value in string t
        # for j in hashmapS:
        #     if hashmapS[j] != hashmapT.get(j, 0): # using .get() function to check if key even exists
        #         return False
        
        # return True

# s[i]: This is indexing into the string s to get the character at position i.
# hashmapS.get(s[i], 0): This is a method call on the dictionary CountS. get() is a method that returns the value associated with the specified key in the dictionary. If the key is not found, it returns the default value specified as the second argument (in this case, 0). So, CountS.get(s[i], 0) tries to get the value associated with the character s[i] in the dictionary CountS, and if the character is not found in the dictionary, it returns 0.
# 1 + hashmapS.get(s[i], 0): This part adds 1 to the value obtained from CountS.get(s[i], 0). If the character s[i] exists in the dictionary, it will add 1 to its current count; otherwise, it adds 1 to 0.
# countS[s[i]] = 1 + CountS.get(s[i], 0): This assigns the result of the expression 1 + CountS.get(s[i], 0) to the key s[i] in the dictionary countS. If s[i] doesn't exist in countS, it creates a new key-value pair with the key s[i] and the value 1 + CountS.get(s[i], 0) (which is 1 if s[i] didn't exist previously, or 1 plus its current count if it did exist).
# So, this expression is essentially updating the count of occurrences of the character s[i] in the dictionary countS. If the character doesn't exist in the dictionary, it initializes its count to 1; otherwise, it increments its current count by 1.