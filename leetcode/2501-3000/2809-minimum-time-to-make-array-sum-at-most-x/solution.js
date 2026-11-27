
var minimumTime = function(nums1, nums2, x) {
    const n = nums1.length;

    let sum1 = 0;
    let sum2 = 0;

    for (let i = 0; i < n; i++) {
        sum1 += nums1[i];
        sum2 += nums2[i];
    }
    const arr = [];

    for (let i = 0; i < n; i++) {
        arr.push([nums1[i], nums2[i]]);
    }

    arr.sort((a, b) => a[1] - b[1]);

    const dp = new Array(n + 1).fill(0);

    for (let i = 0; i < n; i++) {
        const [a, b] = arr[i];

        for (let j = i + 1; j >= 1; j--) {
            dp[j] = Math.max(
                dp[j],
                dp[j - 1] + a + j * b
            );
        }
    }

    for (let t = 0; t <= n; t++) {
        const remainingSum = sum1 + t * sum2 - dp[t];

        if (remainingSum <= x) {
            return t;
        }
    }

    return -1;
};

