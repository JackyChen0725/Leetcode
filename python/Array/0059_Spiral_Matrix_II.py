"""
Link: https://leetcode.com/problems/spiral-matrix-ii/

Solution1: Layer by layer traversal.
    Time complexity: O(n^2).
Solution2: Traversal with direction changing.
    Time complexity: O(n^2).
"""

from typing import List

class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        nums = [[0] * n for _ in range(n)]
        startx, starty = 0, 0
        loop, mid = n // 2, n // 2
        count = 1
        
        for offset in range(1, loop + 1):
            for y in range(starty, n - offset):
                nums[startx][y] = count
                count += 1
            
            for x in range(startx, n - offset):
                nums[x][n - offset] = count
                count += 1
            
            for y in range(n - offset, starty, -1):
                nums[n - offset][y] = count
                count += 1
            
            for x in range(n - offset, startx, -1):
                
                nums[x][starty] = count
                count += 1
            
            startx += 1
            starty += 1
        
        if n % 2 != 0:
            nums[mid][mid] = count
        return nums

class Solution2:
    def generateMatrix(self, n: int) -> List[List[int]]:
        nums = [[0] * n for _ in range(n)]
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        cur_dir_idx = 0
        dx, dy = dirs[cur_dir_idx]
        row, col = 0, 0
        for num in range(1, n * n + 1):
            nums[row][col] = num
            if (row + dx < 0 or row + dx >= n or col + dy < 0 or col + dy >= n) or nums[row + dx][col + dy] > 0:
                cur_dir_idx = (cur_dir_idx + 1) % 4
                dx, dy = dirs[cur_dir_idx]
            row += dx
            col += dy
        return nums