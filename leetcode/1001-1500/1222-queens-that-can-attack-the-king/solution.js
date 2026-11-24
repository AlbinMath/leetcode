var queensAttacktheKing = function(queens, king) {
    // 8x8 board lookup for O(1) queen checks
    const hasQueen = Array.from({ length: 8 }, () => new Uint8Array(8));
    for (const [r, c] of queens) {
        hasQueen[r][c] = 1;
    }

    const attackers = [];
    // Cast rays in all 8 directions starting from the king
    for (let dr = -1; dr <= 1; dr++) {
        for (let dc = -1; dc <= 1; dc++) {
            if (dr === 0 && dc === 0) continue;

            let r = king[0] + dr;
            let c = king[1] + dc;
            while (r >= 0 && r < 8 && c >= 0 && c < 8) {
                if (hasQueen[r][c]) {
                    attackers.push([r, c]);
                    break; // First queen in this direction blocks any behind it
                }
                r += dr;
                c += dc;
            }
        }
    }

    return attackers;
};
