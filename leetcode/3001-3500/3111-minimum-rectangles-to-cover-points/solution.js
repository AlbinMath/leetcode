
var minRectanglesToCoverPoints = function(points, w) {
    const xs = points.map(point => point[0]).sort((a, b) => a - b);

    let count = 0;
    let i = 0;

    while (i < xs.length) {
        const startX = xs[i];

        count++;

        while (i < xs.length && xs[i] <= startX + w) {
            i++;
        }
    }

    return count;
};

