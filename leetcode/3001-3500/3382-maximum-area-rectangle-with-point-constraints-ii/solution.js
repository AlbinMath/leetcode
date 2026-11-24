
var maxRectangleArea = function(xCoord, yCoord) {
    const n = xCoord.length;

    const points = Array.from({ length: n }, (_, i) => [
        xCoord[i],
        yCoord[i]
    ]);

    points.sort((a, b) => a[0] - b[0] || a[1] - b[1]);

    // Coordinate-compress y values.
    const ys = [...new Set(yCoord)].sort((a, b) => a - b);
    const m = ys.length;
    const yIndex = new Map();

    for (let i = 0; i < m; i++) {
        yIndex.set(ys[i], i);
    }

    // Segment tree: maximum x-coordinate seen at each y.
    let size = 1;
    while (size < m) size *= 2;

    const tree = new Array(size * 2).fill(-1);

    function update(pos, value) {
        let i = pos + size;
        tree[i] = value;

        for (i >>= 1; i > 0; i >>= 1) {
            tree[i] = Math.max(tree[i * 2], tree[i * 2 + 1]);
        }
    }

    function rangeMax(left, right) {
        let result = -1;
        left += size;
        right += size;

        while (left <= right) {
            if (left & 1) {
                result = Math.max(result, tree[left++]);
            }

            if (!(right & 1)) {
                result = Math.max(result, tree[right--]);
            }

            left >>= 1;
            right >>= 1;
        }

        return result;
    }

    // Latest x-coordinate where each vertical pair appeared.
    const lastPairX = new Map();
    let answer = -1;

    let start = 0;

    while (start < n) {
        let end = start;

        while (
            end + 1 < n &&
            points[end + 1][0] === points[start][0]
        ) {
            end++;
        }

        const x = points[start][0];

        // Collect y-coordinates in this column.
        const column = [];

        for (let i = start; i <= end; i++) {
            column.push(points[i][1]);
        }

        // Only consecutive points in a column can form
        // an unobstructed vertical rectangle edge.
        for (let i = 0; i + 1 < column.length; i++) {
            const y1 = column[i];
            const y2 = column[i + 1];
            const key = `${y1},${y2}`;

            if (lastPairX.has(key)) {
                const prevX = lastPairX.get(key);
                const low = yIndex.get(y1);
                const high = yIndex.get(y2);

                // No point in the rectangle's y-range
                // may have appeared between prevX and x.
                if (rangeMax(low, high) === prevX) {
                    const area = (x - prevX) * (y2 - y1);
                    answer = Math.max(answer, area);
                }
            }

            lastPairX.set(key, x);
        }

        // Update only after checking every pair in this column.
        for (const y of column) {
            update(yIndex.get(y), x);
        }

        start = end + 1;
    }

    return answer;
};

