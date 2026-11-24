
var minimumMaxValue = function(n, index, value) {
    const smallestPrimeFactor = (x) => {
        if (x % 2 === 0) return 2;
        for (let d = 3; d * d <= x; d += 2) {
            if (x % d === 0) return d;
        }
        return x;
    };

    if (index > 0) {
        if (value === 1) return -1;
        const p = smallestPrimeFactor(value);
        if (value - p <= 2 * (index - 1)) {
            return -1;
        }
    }

    const rightSteps = n - 1 - index;
    if (rightSteps === 0) {
        return value;
    }

    if (value === 1) {
        return -1;
    }

    const p = smallestPrimeFactor(value);
    return value + p + 2 * (rightSteps - 1);
};
