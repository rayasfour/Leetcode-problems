# PROBLEM: VALID SUDOKU
# Determine if a 9 x 9 Sudoku board is valid. 
# Only the filled cells need to be validated according to the following rules:

# Each row must contain the digits 1-9 without repetition.
# Each column must contain the digits 1-9 without repetition.
# Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
# Note:

# A Sudoku board (partially filled) could be valid but is not necessarily solvable.
# Only the filled cells need to be validated according to the mentioned rules.

# SOLUTION 1 [ROUGH IDEA]
class Solution:
    def valid_row(board):
        return True
    def valid_column():
        return True
    def valid_box():
        return True
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        if valid_row(board) and valid_column(board) and valid_box(board):
            return True
        return False

# SOLUTION 2
# Time Complexity O(9^2)
# Memory Complexity O(9^2)
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Create Hashmap
        # The key of hashmap will be the location on the grid
        # The value will be the set of numbers in that box
        # There are nine 3x3 boxes
        cols = collections.defaultdict(set)
        rows = collections.defaultdict(set)
        squares = collections.defaultdict(set)
