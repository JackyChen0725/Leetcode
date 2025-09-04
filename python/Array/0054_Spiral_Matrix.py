"""
Link: https://leetcode.com/problems/spiral-matrix/

Solution: Traversal with direction changing.
    Time complexity: O(m*n).
"""

from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])
        nums = []
        
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        cur_dir_idx = 0
        dx, dy = dirs[cur_dir_idx]
        row, col = 0, 0
        for _ in range(m * n):
            nums.append(matrix[row][col])
            matrix[row][col] = 101
            if (row + dx < 0 or row + dx >= m or col + dy < 0 or col + dy >= n) or matrix[row + dx][col + dy] == 101:
                cur_dir_idx = (cur_dir_idx + 1) % 4
                dx, dy = dirs[cur_dir_idx]
            row += dx
            col += dy
        return nums