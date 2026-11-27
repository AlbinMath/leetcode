
var countCoveredBuildings = function(n, buildings) {
    const rowMin = new Map();
    const rowMax = new Map();
    const colMin = new Map();
    const colMax = new Map();

    for (const [x, y] of buildings) {
        rowMin.set(x, Math.min(rowMin.get(x) ?? Infinity, y));
        rowMax.set(x, Math.max(rowMax.get(x) ?? -Infinity, y));
        colMin.set(y, Math.min(colMin.get(y) ?? Infinity, x));
        colMax.set(y, Math.max(colMax.get(y) ?? -Infinity, x));
    }

    let count = 0;
    for (const [x, y] of buildings) {
        const hasLeft = y > rowMin.get(x);
        const hasRight = y < rowMax.get(x);
        const hasAbove = x > colMin.get(y);
        const hasBelow = x < colMax.get(y);

        if (hasLeft && hasRight && hasAbove && hasBelow) {
            count++;
        }
    }
    return count;
};

