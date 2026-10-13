
var reversePairs = function(nums) {
    const n = nums.length;
    const temp = new Array(n);

    function mergeSort(left, right) {
        if (left >= right) return 0;

        const mid = Math.floor((left + right) / 2);

        let count = mergeSort(left, mid);
        count += mergeSort(mid + 1, right);

        // Count reverse pairs across the two halves
        let j = mid + 1;

        for (let i = left; i <= mid; i++) {
            while (
                j <= right &&
                nums[i] > 2 * nums[j]
            ) {
                j++;
            }

            count += j - (mid + 1);
        }

        // Merge the two sorted halves
        let i = left;
        j = mid + 1;
        let k = left;

        while (i <= mid && j <= right) {
            if (nums[i] <= nums[j]) {
                temp[k++] = nums[i++];
            } else {
                temp[k++] = nums[j++];
            }
        }

        while (i <= mid) {
            temp[k++] = nums[i++];
        }

        while (j <= right) {
            temp[k++] = nums[j++];
        }

        for (let p = left; p <= right; p++) {
            nums[p] = temp[p];
        }

        return count;
    }

    return mergeSort(0, n - 1);
};

