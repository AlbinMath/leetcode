/**
 * @param {number[]} nums
 * @return {number[]}
 */
var maximumMEX = function (nums) {
    const n = nums.length;

    // suf[i] = mex of nums[i..n-1]
    const suf = new Array(n + 1).fill(0);
    const present = new Uint8Array(n + 2);
    let mex = 0;
    for (let i = n - 1; i >= 0; i--) {
        if (nums[i] <= n) present[nums[i]] = 1;
        while (present[mex]) mex++;
        suf[i] = mex;
    }

    const res = [];
    const stamp = new Int32Array(n + 2).fill(-1);
    let seg = 0, i = 0;

    while (i < n) {
        const M = suf[i];
        if (M === 0) {
            res.push(0);
            i++;
            continue;
        }
        let cnt = 0;
        while (cnt < M) {
            const v = nums[i];
            if (v < M && stamp[v] !== seg) {
                stamp[v] = seg;
                cnt++;
            }
            i++;
        }
        res.push(M);
        seg++;
    }
    return res;
};
