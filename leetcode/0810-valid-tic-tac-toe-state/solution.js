var validTicTacToe = function(board) {
    let xCount = 0;
    let oCount = 0;

    for (let r = 0; r < 3; r++) {
        for (let c = 0; c < 3; c++) {
            if (board[r][c] === 'X') xCount++;
            else if (board[r][c] === 'O') oCount++;
        }
    }

    // Turn order check: X moves first, so xCount is either oCount or oCount + 1
    if (xCount !== oCount && xCount !== oCount + 1) {
        return false;
    }

    const hasWon = (p) => {
        for (let i = 0; i < 3; i++) {
            if (board[i][0] === p && board[i][1] === p && board[i][2] === p) return true;
            if (board[0][i] === p && board[1][i] === p && board[2][i] === p) return true;
        }
        return (
            (board[0][0] === p && board[1][1] === p && board[2][2] === p) ||
            (board[0][2] === p && board[1][1] === p && board[2][0] === p)
        );
    };

    const xWins = hasWon('X');
    const oWins = hasWon('O');

    // If X won, the game ended on X's turn
    if (xWins && xCount !== oCount + 1) return false;
    // If O won, the game ended on O's turn
    if (oWins && xCount !== oCount) return false;

    return true;
};
