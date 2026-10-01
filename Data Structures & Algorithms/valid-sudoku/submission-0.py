class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Dict for row and column counts
        # For every board[row][column], add row[row], column[col]
        # Each row and col must sum to 45

        row_counts, col_counts, sub_grid_counts = defaultdict(list), defaultdict(list), defaultdict(list)
        for row_idx, row in enumerate(board):
            for col_idx, digit in enumerate(row):
                if digit == ".": 
                    continue
                digit = int(digit)
                if (digit in row_counts[row_idx])\
                or (digit in col_counts[col_idx])\
                or (digit in sub_grid_counts[row_idx // 3, col_idx // 3]):
                    return False

                row_counts[row_idx].append(digit)
                col_counts[col_idx].append(digit)
                sub_grid_counts[row_idx // 3, col_idx // 3].append(digit)

        return True

