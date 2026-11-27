
var maxConsecutive = function(bottom, top, special) {
    special.sort((a, b) => a - b);

    let maxGap = 0;
    let previous = bottom - 1;

    for (const floor of special) {
        const gap = floor - previous - 1;

        maxGap = Math.max(maxGap, gap);
        previous = floor;
    }
    const lastGap = top - previous;

    maxGap = Math.max(maxGap, lastGap);

    return maxGap;
};

