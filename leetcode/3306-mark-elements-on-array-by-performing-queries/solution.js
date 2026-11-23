var unmarkedSumArray = function(nums, queries) {
    const n = nums.length;
    let totalSum = 0;
    for (const num of nums) totalSum += num;

    const marked = new Uint8Array(n);
    const sortedIndices = Array.from({ length: n }, (_, i) => i);
    sortedIndices.sort((a, b) => (nums[a] !== nums[b] ? nums[a] - nums[b] : a - b));

    let ptr = 0;
    const answer = new Array(queries.length);

    for (let q = 0; q < queries.length; q++) {
        let [idx, k] = queries[q];

        if (!marked[idx]) {
            marked[idx] = 1;
            totalSum -= nums[idx];
        }

        while (k > 0 && ptr < n) {
            const cand = sortedIndices[ptr++];
            if (!marked[cand]) {
                marked[cand] = 1;
                totalSum -= nums[cand];
                k--;
            }
        }

        answer[q] = totalSum;
    }

    return answer;
};
