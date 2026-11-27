
var maxSumDistinctTriplet = function(x, y) {
    const maxY = new Map();

    for (let i = 0; i < x.length; i++) {
        maxY.set(
            x[i],
            Math.max(maxY.get(x[i]) || 0, y[i])
        );
    }

    const values = [...maxY.values()].sort((a, b) => b - a);

    if (values.length < 3) {
        return -1;
    }

    return values[0] + values[1] + values[2];
};

