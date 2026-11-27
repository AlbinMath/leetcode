
var checkValidCuts = function(n, rectangles) {
    const canMakeCuts = function(axis) {
        const intervals = rectangles.map(rect => [
            rect[axis],
            rect[axis + 2]
        ]);
        intervals.sort((a, b) => a[0] - b[0]);
        let groups = 0;
        let currentEnd = -1;

        for (const [start, end] of intervals) {
            if (start >= currentEnd) {
                groups++;
                currentEnd = end;
            } else {
                currentEnd = Math.max(currentEnd, end);
            }
            if (groups >= 3) {
                return true;
            }
        }
        return false;
    };
    return canMakeCuts(0) || canMakeCuts(1);
};

