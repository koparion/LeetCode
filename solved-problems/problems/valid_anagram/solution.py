class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) == len(t):
            stringS = {}
            stringT= {}

            for i in range(len(s)):
                stringS[s[i]] = 1 + stringS.get(s[i], 0)
                stringT[t[i]] = 1 + stringT.get(t[i], 0)
            return stringS == stringT
        
        return False
        