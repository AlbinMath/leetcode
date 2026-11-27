
var maximumTotalSum = function(maximumHeight) {
    maximumHeight.sort((a, b) => b - a);

    let totalSum = 0;
    let previousHeight = Infinity;

    for (const maxHeight of maximumHeight) {
        const height = Math.min(maxHeight, previousHeight - 1);
        if (height <= 0) {
            return -1;
        }

        totalSum += height;
        previousHeight = height;
    }

    return totalSum;
};

