
var minCost = function(arr, brr, k) {
    const n = arr.length;
    let directCost = 0;

    for (let i = 0; i < n; i++) {
        directCost += Math.abs(arr[i] - brr[i]);
    }
    const sortedArr = [...arr].sort((a, b) => a - b);
    const sortedBrr = [...brr].sort((a, b) => a - b);

    let rearrangedCost = k;

    for (let i = 0; i < n; i++) {
        rearrangedCost += Math.abs(sortedArr[i] - sortedBrr[i]);
    }

    return Math.min(directCost, rearrangedCost);
};

