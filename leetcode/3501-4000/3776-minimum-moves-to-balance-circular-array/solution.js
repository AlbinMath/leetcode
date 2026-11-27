var minMoves = function(balance) {
    const n = balance.length;

    let total = 0;
    let negativeIndex = -1;

    for (let i = 0; i < n; i++) {
        total += balance[i];

        if (balance[i] < 0) {
            negativeIndex = i;
        }
    }

    if (total < 0) return -1;

    if (negativeIndex === -1) return 0;

    let needed = -balance[negativeIndex];
    let moves = 0;

    for (let distance = 1; distance <= Math.floor(n / 2); distance++) {
        const left = (negativeIndex - distance + n) % n;
        const right = (negativeIndex + distance) % n;

        const indices = left === right ? [left] : [left, right];

        for (const index of indices) {
            const available = balance[index];
            const take = Math.min(needed, available);

            moves += take * distance;
            needed -= take;

            if (needed === 0) return moves;
        }
    }

    return -1;
};
