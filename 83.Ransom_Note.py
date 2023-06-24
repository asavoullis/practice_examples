# 83. Ransom Note
# Given two strings ransomNote and magazine, return true 
# if ransomNote can be constructed by using the letters from magazine and false otherwise.
# Each letter in magazine can only be used once in ransomNote.

# Example 1:
# Input: ransomNote = "a", magazine = "b"
# Output: false

# Example 2:
# Input: ransomNote = "aa", magazine = "ab"
# Output: false

# Example 3:
# Input: ransomNote = "aa", magazine = "aab"
# Output: true
 

# Constraints:
# 1 <= ransomNote.length, magazine.length <= 105
# ransomNote and magazine consist of lowercase English letters.

class Solution:
    # O(N) where N is ransomNote
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        for i in ransomNote:
            if i in magazine:
                # string.replace(oldvalue, newvalue, count)
                magazine = magazine.replace(i,"",1)
            else:
                return False
        return True


    def canConstruct_faster(self, ransomNote: str, magazine: str) -> bool:
        for i in set(ransomNote):
            # if the number of times the letter is less in magazine than in ransomNote
            if magazine.count(i) < ransomNote.count(i):
                return False
        return True


    def canConstruct_slow(self, ransomNote: str, magazine: str) -> bool:

        hashmap = {}

        for i in range(len(magazine)):
            if magazine[i] in hashmap:
                hashmap[magazine[i]] += 1
            else:
                hashmap[magazine[i]] = 1

        for a in range(len(ransomNote)):
            if ransomNote[a] in hashmap and hashmap[ransomNote[a]] > 0:
                hashmap[ransomNote[a]] -= 1
            else:
                return False
        
        return True


ransomNote1 = "aa"
magazine1 = "ab"

ransomNote2 = "aa"
magazine2 = "aab"


sol = Solution().canConstruct(ransomNote2,magazine2)
print(sol)