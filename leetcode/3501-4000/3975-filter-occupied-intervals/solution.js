var filterOccupiedIntervals = function(occupiedIntervals, freeStart, freeEnd) {
    occupiedIntervals.sort((a, b) => a[0] - b[0]);
    const merged = [];
    for (const [start, end] of occupiedIntervals) {
        if (
            merged.length === 0 ||
            start > merged[merged.length - 1][1] + 1
        ) {
            merged.push([start, end]);
        } else {
            merged[merged.length - 1][1] = Math.max(
                merged[merged.length - 1][1],
                end
            );
        }
    }
    const result = [];
    for (const [start, end] of merged) {
        if (end < freeStart || start > freeEnd) {
            result.push([start, end]);
            continue;
        }
        if (start < freeStart) {
            result.push([start, freeStart - 1]);
        }
        if (end > freeEnd) {
            result.push([freeEnd + 1, end]);
        }
    }
    return result;
};

