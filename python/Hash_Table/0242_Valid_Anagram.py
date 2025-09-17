"""
Link: https://leetcode.com/problems/valid-anagram/

Solution1: Use a defaultdict to count character occurrences.
    Time Complexity: O(n).
    Space Complexity: O(1) (since the character set is limited).

Solution2: Use two defaultdicts to count character occurrences in both strings and compare.
    Time Complexity: O(n).
    Space Complexity: O(1) (since the character set is limited).

Solution3: Use a Counter to count character occurrences and compare.
    Time Complexity: O(n).
    Space Complexity: O(1) (since the character set is limited).
"""

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        from collections import defaultdict
        letterDict = defaultdict(int)

        for c in s:
            letterDict[c] += 1
        
        for c in t:
            letterDict[c] -= 1
            if letterDict[c] < 0:
                return False
            if letterDict[c] == 0:
                del letterDict[c]

        return len(letterDict) == 0

class Solution2:
    def isAnagram(self, s: str, t: str) -> bool:
        from collections import defaultdict
        s_dict = defaultdict(int)
        t_dict = defaultdict(int)
        
        for c in s:
            s_dict[c] += 1
            
        for c in t:
            t_dict[c] += 1
        
        return s_dict == t_dict

class Solution3:
    def isAnagram(self, s: str, t: str) -> bool:
        from collections import Counter
        return Counter(s) == Counter(t)

s = "anagram"
t = "nagaram"
print(Solution().isAnagram(s, t))