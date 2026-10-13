
var countRangeSum = function(nums, lower, upper) {
    const n = nums.length;
    const prefix = new Array(n + 1).fill(0);

    for (let i = 0; i < n; i++) {
        prefix[i + 1] = prefix[i] + nums[i];
    }

    const temp = new Array(n + 1);

    function mergeSort(left, right) {
        if (left >= right) return 0;

        const mid = Math.floor((left + right) / 2);
        let count = mergeSort(left, mid) +
                    mergeSort(mid + 1, right);

        let low = mid + 1;
        let high = mid + 1;

        // Count valid ranges crossing the midpoint
        for (let i = left; i <= mid; i++) {
            while (
                low <= right &&
                prefix[low] - prefix[i] < lower
            ) {
                low++;
            }

            while (
                high <= right &&
                prefix[high] - prefix[i] <= upper
            ) {
                high++;
            }

            count += high - low;
        }

        // Merge both sorted halves
        let i = left;
        let j = mid + 1;
        let k = left;

        while (i <= mid && j <= right) {
            if (prefix[i] <= prefix[j]) {
                temp[k++] = prefix[i++];
            } else {
                temp[k++] = prefix[j++];
            }
        }

        while (i <= mid) {
            temp[k++] = prefix[i++];
        }

        while (j <= right) {
            temp[k++] = prefix[j++];
        }

        for (let p = left; p <= right; p++) {
            prefix[p] = temp[p];
        }

        return count;
    }

    return mergeSort(0, n);
};

