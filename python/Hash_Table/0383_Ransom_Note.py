"""
Link: https://leetcode.com/problems/ransom-note/

Solution1: Use a fixed-size array (hash) to track presence of elements since the range is known (0 to 25 for lowercase letters).
    Time Complexity: O(n + m) where n and m are the lengths of ransomNote and magazine.
    Space Complexity: O(1).

Solution2: Use a dictionary to count character occurrences.
    Time Complexity: O(n + m) where n and m are the lengths of ransomNote and magazine.
    Space Complexity: O(1).
"""

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        arr = [0] * 26
        
        for c in magazine:
            arr[ord(c) - ord('a')] += 1
        
        for c in ransomNote:
            arr[ord(c) - ord('a')] -= 1
            if arr[ord(c) - ord('a')] < 0:
                return False
        return True

class Solution2:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        hash = dict()
        
        for c in magazine:
            hash[c] = hash.get(c, 0) + 1
        
        for c in ransomNote:
            if c not in hash or hash[c] == 0:
                return False
            hash[c] -= 1
        return True

print(Solution().canConstruct("ab", "aab"))