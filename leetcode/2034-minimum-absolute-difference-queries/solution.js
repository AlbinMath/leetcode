var minDifference = function(nums, queries) {
    const n = nums.length;
    let prefix = Array.from(
        { length: 101 },
        () => new Int32Array(n + 1)
    );
    for (let v = 1; v <= 100; v++) {
        for (let i = 0; i < n; i++) {
            prefix[v][i + 1] =
                prefix[v][i] + (nums[i] === v ? 1 : 0);
        }
    }
    let answer = [];
    for (let [left, right] of queries) {
        let minDiff = Infinity;
        let previous = -1;
        for (let v = 1; v <= 100; v++) {
            let count =
                prefix[v][right + 1] - prefix[v][left];

            if (count > 0) {
                if (previous !== -1) {
                    minDiff = Math.min(
                        minDiff,
                        v - previous
                    );
                }

                previous = v;
            }
        }

        answer.push(minDiff === Infinity ? -1 : minDiff);
    }

    return answer;
};
