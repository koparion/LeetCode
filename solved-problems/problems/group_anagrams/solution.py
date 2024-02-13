class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}

        for word in strs: # counting the frequency of each character in the word
            count = [0] * 26 # there are 26 characters from a to z, so we need to initalize a list to count frequencies
            
            for char in word:
                count[ord(char) - ord('a')] += 1 # Increment the count for the character
                    ### ord() function in Python returns the Unicode code point for a given character. It takes a single Unicode character as a parameter 
                    ### and returns its integer code point. For example, ord('a') returns the integer 97 because 'a' has the Unicode code point 97.
            count_tuples = tuple(count) # Convert the count list to a tuple to use it as a dictionary key

            if count_tuples in hashmap: # if the count tuples has already a key in the dictionary, append to the original word
                hashmap[count_tuples].append(word)
            else: # otherwise, create a new key with the count tuples and initialize its value with a list containing the original word
                hashmap[count_tuples] = [word]

        return list(hashmap.values()) # we need to return the values of the dictionary, which will be the lists of anagrams