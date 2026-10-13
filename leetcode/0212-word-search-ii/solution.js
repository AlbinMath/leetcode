
var findWords = function(board, words) {
    const root = {};

    // Build the Trie
    for (const word of words) {
        let node = root;

        for (const char of word) {
            if (!node[char]) {
                node[char] = {};
            }
            node = node[char];
        }

        node.word = word;
    }

    const m = board.length;
    const n = board[0].length;
    const result = [];

    function dfs(row, col, node) {
        const char = board[row][col];
        const nextNode = node[char];

        if (!nextNode) return;

        // Found a complete word
        if (nextNode.word !== undefined) {
            result.push(nextNode.word);

            // Prevent finding the same word again
            nextNode.word = undefined;
        }

        // Mark this cell as visited
        board[row][col] = "#";

        const directions = [
            [1, 0],
            [-1, 0],
            [0, 1],
            [0, -1]
        ];

        for (const [dr, dc] of directions) {
            const nr = row + dr;
            const nc = col + dc;

            if (
                nr >= 0 &&
                nr < m &&
                nc >= 0 &&
                nc < n &&
                board[nr][nc] !== "#"
            ) {
                dfs(nr, nc, nextNode);
            }
        }

        // Restore the original character
        board[row][col] = char;
    }

    // Start DFS from every cell
    for (let row = 0; row < m; row++) {
        for (let col = 0; col < n; col++) {
            dfs(row, col, root);
        }
    }

    return result;
};

