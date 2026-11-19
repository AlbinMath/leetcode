from typing import List

class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        m, n = len(board), len(board[0])
        r, c = click
        
        if board[r][c] == 'M':
            board[r][c] = 'X'
            return board
            
        dirs = ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1))
        
        def dfs(cr: int, cc: int) -> None:
            mines = 0
            for dr, dc in dirs:
                nr, nc = cr + dr, cc + dc
                if 0 <= nr < m and 0 <= nc < n and board[nr][nc] == 'M':
                    mines += 1
                    
            if mines > 0:
                board[cr][cc] = str(mines)
                return
                
            board[cr][cc] = 'B'
            for dr, dc in dirs:
                nr, nc = cr + dr, cc + dc
                if 0 <= nr < m and 0 <= nc < n and board[nr][nc] == 'E':
                    dfs(nr, nc)
                    
        dfs(r, c)
        return board
