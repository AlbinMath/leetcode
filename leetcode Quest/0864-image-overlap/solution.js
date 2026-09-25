/**
 * @param {number[][]} img1
 * @param {number[][]} img2
 * @return {number}
 */
var largestOverlap = function(img1, img2) {
    const n = img1.length;
    let maxOverlap = 0;

    // Try every possible translation
    for (let dr = -(n - 1); dr <= n - 1; dr++) {
        for (let dc = -(n - 1); dc <= n - 1; dc++) {

            let overlap = 0;

            for (let i = 0; i < n; i++) {
                for (let j = 0; j < n; j++) {

                    let x = i + dr;
                    let y = j + dc;

                    // Check if translated position is inside img2
                    if (x >= 0 && x < n && y >= 0 && y < n) {
                        if (img1[i][j] === 1 && img2[x][y] === 1) {
                            overlap++;
                        }
                    }
                }
            }

            maxOverlap = Math.max(maxOverlap, overlap);
        }
    }

    return maxOverlap;
};
