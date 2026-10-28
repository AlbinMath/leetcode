/**
 * @param {number[]} nums
 * @param {number[]} andValues
 * @return {number}
 */
var minimumValueSum = function (nums, andValues) {
    const n = nums.length, m = andValues.length;
    let prev = new Array(n + 1).fill(Infinity);
    prev[0] = 0; // zero subarrays cover zero elements

    for (let j = 1; j <= m; j++) {
        const target = andValues[j - 1];
        const cur = new Array(n + 1).fill(Infinity);
        let groups = []; // [andValue, minPrev], ordered by start index

        for (let i = 1; i <= n; i++) {
            const x = nums[i - 1];
            const next = [];
            const push = (a, b) => {
                const last = next[next.length - 1];
                if (last && last[0] === a) {
                    if (b < last[1]) last[1] = b;
                } else {
                    next.push([a, b]);
                }
            };
            for (const [a, b] of groups) push(a & x, b);
            push(x, prev[i - 1]); // new subarray starting at index i-1
            groups = next;

            for (const [a, b] of groups) {
                if (a === target && b < Infinity) {
                    cur[i] = b + x;
                    break;
                }
            }
        }
        prev = cur;
    }
    return prev[n] === Infinity ? -1 : prev[n];
};
