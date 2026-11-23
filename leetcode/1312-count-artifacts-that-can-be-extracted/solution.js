var digArtifacts = function(n, artifacts, dig) {
    // Encode 2D coordinates (r, c) into a unique 1D integer: r * n + c
    const dugCells = new Set();
    for (const [r, c] of dig) {
        dugCells.add(r * n + c);
    }

    let extractableCount = 0;

    for (const [r1, c1, r2, c2] of artifacts) {
        let canExtract = true;

        for (let r = r1; r <= r2; r++) {
            for (let c = c1; c <= c2; c++) {
                if (!dugCells.has(r * n + c)) {
                    canExtract = false;
                    break;
                }
            }
            if (!canExtract) break;
        }

        if (canExtract) {
            extractableCount++;
        }
    }

    return extractableCount;
};
