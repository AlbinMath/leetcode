
/**
 * @param {number} m
 * @param {number} n
 * @param {number} introvertsCount
 * @param {number} extrovertsCount
 * @return {number}
 */
var getMaxGridHappiness = function(
    m,
    n,
    introvertsCount,
    extrovertsCount
) {
    const BASE_INTRO = 120;
    const BASE_EXTRO = 40;

    // Combined happiness change caused by one adjacent pair.
    const interaction = [
        [0, 0, 0],
        [0, -60, -10],
        [0, -10, 40]
    ];

    const totalCells = m * n;
    const maskSize = 3 ** n;
    const highestPlace = 3 ** (n - 1);
    const memo = new Map();

    function dfs(pos, intro, extro, mask) {
        if (pos === totalCells) {
            return 0;
        }

        const key = `${pos},${intro},${extro},${mask}`;

        if (memo.has(key)) {
            return memo.get(key);
        }

        const col = pos % n;
        const row = Math.floor(pos / n);

        // The most significant base-3 digit is the cell above.
        const above = row > 0
            ? Math.floor(mask / highestPlace)
            : 0;

        // The least significant digit is the cell to the left.
        const left = col > 0 ? mask % 3 : 0;

        // Option 1: Leave this cell empty.
        const nextMaskEmpty = (mask * 3) % maskSize;
        let best = dfs(pos + 1, intro, extro, nextMaskEmpty);

        // Option 2: Place an introvert.
        if (intro > 0) {
            let happiness = BASE_INTRO;

            happiness += interaction[1][above];
            happiness += interaction[1][left];

            const nextMask = (mask * 3 + 1) % maskSize;

            best = Math.max(
                best,
                happiness + dfs(
                    pos + 1,
                    intro - 1,
                    extro,
                    nextMask
                )
            );
        }

        // Option 3: Place an extrovert.
        if (extro > 0) {
            let happiness = BASE_EXTRO;

            happiness += interaction[2][above];
            happiness += interaction[2][left];

            const nextMask = (mask * 3 + 2) % maskSize;

            best = Math.max(
                best,
                happiness + dfs(
                    pos + 1,
                    intro,
                    extro - 1,
                    nextMask
                )
            );
        }

        memo.set(key, best);
        return best;
    }

    return dfs(
        0,
        introvertsCount,
        extrovertsCount,
        0
    );
};

