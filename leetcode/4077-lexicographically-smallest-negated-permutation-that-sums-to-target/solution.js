var lexSmallestNegatedPerm = function(n, target) {
    const total = (n * (n + 1)) / 2;

    if (target < -total || target > total) {
        return [];
    }

    if ((total - target) % 2 !== 0) {
        return [];
    }

    let remaining = (total - target) / 2;

    const negative = [];
    const positive = [];

    for (let i = n; i >= 1; i--) {
        if (remaining >= i) {
            negative.push(-i);
            remaining -= i;
        } else {
            positive.push(i);
        }
    }

    positive.reverse();

    return [...negative, ...positive];
};
