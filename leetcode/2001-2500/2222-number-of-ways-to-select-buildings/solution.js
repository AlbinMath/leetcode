var numberOfWays = function(s) {
    let totalZeros = 0;
    let totalOnes = 0;
    for (let ch of s) {
        if (ch === '0') {
            totalZeros++;
        } else {
            totalOnes++;
        }
    }
    let leftZeros = 0;
    let leftOnes = 0;
    let result = 0;

    for (let ch of s) {
        if (ch === '0') {
            let rightOnes = totalOnes - leftOnes;
            result += leftOnes * rightOnes;
            leftZeros++;
        } else {
            let rightZeros = totalZeros - leftZeros;
            result += leftZeros * rightZeros;
            leftOnes++;
        }
    }
    return result;
};
