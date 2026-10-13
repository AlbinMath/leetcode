
var snakesAndLadders = function(board) {
    const n = board.length;
    const target = n * n;

    // Convert square label to board coordinates
    function getCoordinates(square) {
        const rowFromBottom = Math.floor((square - 1) / n);
        const row = n - 1 - rowFromBottom;

        let col = (square - 1) % n;

        // Rows alternate direction (Boustrophedon)
        if (rowFromBottom % 2 === 1) {
            col = n - 1 - col;
        }

        return [row, col];
    }

    const queue = [[1, 0]]; // [square, dice rolls]
    const visited = new Set([1]);
    let front = 0;

    while (front < queue.length) {
        const [square, rolls] = queue[front++];

        if (square === target) {
            return rolls;
        }

        // Try every possible dice roll
        for (
            let next = square + 1;
            next <= Math.min(square + 6, target);
            next++
        ) {
            const [row, col] = getCoordinates(next);

            // Take at most one snake or ladder
            const destination =
                board[row][col] === -1
                    ? next
                    : board[row][col];

            if (!visited.has(destination)) {
                visited.add(destination);
                queue.push([destination, rolls + 1]);
            }
        }
    }

    return -1;
};

