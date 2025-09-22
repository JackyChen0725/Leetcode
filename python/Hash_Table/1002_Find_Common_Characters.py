"""
Link: https://leetcode.com/problems/find-common-characters/

Solution1: Use two frequency arrays to count character occurrences.
    Time Complexity: O(n * m) where n is the number of words and m is the length of the longest word.
    Space Complexity: O(m).

Solution2: Use two Counters to count character occurrences and intersect them.
    Time Complexity: O(n * m) where n is the number of words and m is the length of the longest word.
    Space Complexity: O(m).
"""

from typing import List

class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        def count(word):
            frequency = [0] * 26
            for c in word:
                frequency[ord(c) - ord('a')] += 1
            return frequency
        
        freq1 = count(words[0])
        
        for word in words[1:]:
            freq2 = count(word)
            for i in range(26):
                freq1[i] = min(freq1[i], freq2[i])
        
        res = []
        for i in range(26):
            res.extend([chr(i + ord('a'))] * freq1[i])
        
        return res

class Solution2:
    def commonChars(self, words: List[str]) -> List[str]:
        from collections import Counter
        
        freq1 = Counter(words[0])
        
        for word in words[1:]:
            freq2 = Counter(word)
            freq1 &= freq2
        
        res = []
        for k, v in freq1.items():
            res.extend([k] * v)
        
        return res