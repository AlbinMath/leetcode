var findRightInterval = function(intervals) {
    const n = intervals.length;
    const starts = [];

    for (let i = 0; i < n; i++) {
        starts.push([intervals[i][0], i]);
    }

    starts.sort((a, b) => a[0] - b[0]);

    const result = [];

    for (let i = 0; i < n; i++) {
        const target = intervals[i][1];
        let left = 0;
        let right = n - 1;
        let ans = -1;

        while (left <= right) {
            const mid = Math.floor((left + right) / 2);

            if (starts[mid][0] >= target) {
                ans = starts[mid][1];
                right = mid - 1;
            } else {
                left = mid + 1;
            }
        }

        result.push(ans);
    }

    return result;
};
