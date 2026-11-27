
var minimumCost = function(m, n, horizontalCut, verticalCut) {
    horizontalCut.sort((a, b) => b - a);
    verticalCut.sort((a, b) => b - a);

    let i = 0;
    let j = 0;

    let horizontalPieces = 1;
    let verticalPieces = 1;

    let totalCost = 0;

    while (i < horizontalCut.length && j < verticalCut.length) {
        if (horizontalCut[i] >= verticalCut[j]) {
            totalCost += horizontalCut[i] * verticalPieces;
            horizontalPieces++;
            i++;
        } else {
            totalCost += verticalCut[j] * horizontalPieces;
            verticalPieces++;
            j++;
        }
    }
    while (i < horizontalCut.length) {
        totalCost += horizontalCut[i] * verticalPieces;
        horizontalPieces++;
        i++;
    }
    while (j < verticalCut.length) {
        totalCost += verticalCut[j] * horizontalPieces;
        verticalPieces++;
        j++;
    }

    return totalCost;
};

