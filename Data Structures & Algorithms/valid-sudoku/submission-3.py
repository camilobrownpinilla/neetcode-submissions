from copy import deepcopy as copy

class Solution:
    def getBox(self, x: int, y: int) -> tuple[int, int]:
        x_level = x // 3
        y_level = y // 3
        return (x_level, y_level)

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = {i: [] for i in range(9)}
        cols = copy(rows)
        boxes = {(i,j): [] for i in range(3) for j in range(3)}


        for i, row in enumerate(board):
            for j, char in enumerate(row):
                if char == '.':
                    continue
                else:
                    box = self.getBox(i,j)
                    if char not in rows[i]:
                        rows[i].append(char)
                    else:
                        return False

                    if char not in cols[j]:
                        cols[j].append(char)
                    else:
                        return False
                        
                    if char not in boxes[box]:
                        boxes[box].append(char)
                    else:
                        return False
        return True

                    
                     
        