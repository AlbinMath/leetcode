var areSimilar = function(mat, k) {
    const n = mat[0].length;
    const shift = k % n;

    if (shift === 0) return true;

    for (const row of mat) {
        for (let j = 0; j < n; j++) {
            if (row[j] !== row[(j + shift) % n]) {
                return false;
            }
        }
    }

    return true;
};
