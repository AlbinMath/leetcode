var minimumCost = function(s, t, flipCost, swapCost, crossCost) {
    let countA = 0;
    let countB = 0;

    for (let i = 0; i < s.length; i++) {
        if (s[i] !== t[i]) {
            if (s[i] === '0') {
                countA++;
            } else {
                countB++;
            }
        }
    }

    if (countA + countB === 0) {
        return 0;
    }

    const pairCost = Math.min(swapCost, 2 * flipCost);

    const samePairCost = Math.min(
        crossCost + swapCost,
        2 * flipCost
    );
    const oppositePairs = Math.min(countA, countB);

    let totalCost = oppositePairs * pairCost;

    const remaining = Math.abs(countA - countB);

    totalCost += Math.floor(remaining / 2) * samePairCost;

    if (remaining % 2 === 1) {
        totalCost += flipCost;
    }

    return totalCost;
};
