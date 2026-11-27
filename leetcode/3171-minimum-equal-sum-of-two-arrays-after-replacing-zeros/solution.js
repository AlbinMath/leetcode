var minSum = function(nums1, nums2) {
    let sum1 = 0;
    let sum2 = 0;

    let zeros1 = 0;
    let zeros2 = 0;

    for (let num of nums1) {
        sum1 += num;

        if (num === 0) zeros1++;
    }

    for (let num of nums2) {
        sum2 += num;

        if (num === 0) zeros2++;
    }

    let minSum1 = sum1 + zeros1;
    let minSum2 = sum2 + zeros2;

    if (zeros1 > 0 && zeros2 > 0) {
        return Math.max(minSum1, minSum2);
    }

    if (zeros1 > 0) {
        return minSum1 <= sum2 ? sum2 : -1;
    }

    if (zeros2 > 0) {
        return minSum2 <= sum1 ? sum1 : -1;
    }

    return sum1 === sum2 ? sum1 : -1;
};
