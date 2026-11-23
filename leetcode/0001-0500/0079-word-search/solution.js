var exist = function(board, word) {
    const rows = board.length;
    const cols = board[0].length;

    function dfs(r, c, index) {
        // All characters matched
        if (index === word.length) {
            return true;
        }

        // Out of bounds or character doesn't match
        if (
            r < 0 || r >= rows ||
            c < 0 || c >= cols ||
            board[r][c] !== word[index]
        ) {
            return false;
        }

        // Mark the cell as visited
        const temp = board[r][c];
        board[r][c] = "#";

        // Explore four adjacent cells
        const found =
            dfs(r + 1, c, index + 1) ||
            dfs(r - 1, c, index + 1) ||
            dfs(r, c + 1, index + 1) ||
            dfs(r, c - 1, index + 1);

        // Restore the original character
        board[r][c] = temp;

        return found;
    }

    for (let r = 0; r < rows; r++) {
        for (let c = 0; c < cols; c++) {
            if (dfs(r, c, 0)) {
                return true;
            }
        }
    }

    return false;
};
