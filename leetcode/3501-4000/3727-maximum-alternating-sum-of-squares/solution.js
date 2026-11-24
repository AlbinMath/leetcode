
var maxAlternatingSum = function(nums) {
    const squares = nums
        .map(num => num * num)
        .sort((a, b) => a - b);

    let score = 0;
    const n = squares.length;
    const positiveCount = Math.ceil(n / 2);

    for (let i = 0; i < n; i++) {
        if (i < positiveCount) {
            score += squares[n - 1 - i];
        } else {
            score -= squares[i - positiveCount];
        }
    }

    return score;
};

