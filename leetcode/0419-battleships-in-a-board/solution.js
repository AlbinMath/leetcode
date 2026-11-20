var countBattleships = function(board) {
    const m = board.length;
    const n = board[0].length;
    let ships = 0;

    for (let r = 0; r < m; r++) {
        for (let c = 0; c < n; c++) {
            if (board[r][c] === 'X') {
                // Count only if this cell has no 'X' immediately above or to its left
                const noTop = r === 0 || board[r - 1][c] !== 'X';
                const noLeft = c === 0 || board[r][c - 1] !== 'X';
                if (noTop && noLeft) {
                    ships++;
                }
            }
        }
    }

    return ships;
};
