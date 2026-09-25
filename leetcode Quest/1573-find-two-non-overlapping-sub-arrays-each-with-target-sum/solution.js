var minSumOfLengths = function(arr, target) {
    const n = arr.length;
    const best = new Array(n).fill(Infinity);

    let left = 0;
    let sum = 0;
    let minLen = Infinity;
    let answer = Infinity;

    for (let right = 0; right < n; right++) {
        sum += arr[right];

        while (sum > target && left <= right) {
            sum -= arr[left];
            left++;
        }

        // Subarray [left ... right] has sum = target
        if (sum === target) {
            const len = right - left + 1;

            // Combine with a previous non-overlapping subarray
            if (left > 0 && best[left - 1] !== Infinity) {
                answer = Math.min(answer, len + best[left - 1]);
            }

            minLen = Math.min(minLen, len);
        }

        // Best subarray ending at or before right
        best[right] = minLen;
    }

    return answer === Infinity ? -1 : answer;
};
