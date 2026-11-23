
var solve = function(board) {
    const m = board.length;
    const n = board[0].length;

    function dfs(row, col) {
        if (
            row < 0 ||
            row >= m ||
            col < 0 ||
            col >= n ||
            board[row][col] !== "O"
        ) {
            return;
        }

        // Preserve boundary-connected regions
        board[row][col] = "#";

        dfs(row - 1, col); // Up
        dfs(row + 1, col); // Down
        dfs(row, col - 1); // Left
        dfs(row, col + 1); // Right
    }

    // Explore the first and last columns
    for (let row = 0; row < m; row++) {
        dfs(row, 0);
        dfs(row, n - 1);
    }

    // Explore the first and last rows
    for (let col = 0; col < n; col++) {
        dfs(0, col);
        dfs(m - 1, col);
    }

    // Capture surrounded regions and restore safe regions
    for (let row = 0; row < m; row++) {
        for (let col = 0; col < n; col++) {
            if (board[row][col] === "O") {
                board[row][col] = "X";
            } else if (board[row][col] === "#") {
                board[row][col] = "O";
            }
        }
    }
};

