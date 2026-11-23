
var countSmaller = function(nums) {
    const n = nums.length;
    const counts = new Array(n).fill(0);

    // Store original indices alongside values
    const indices = nums.map((_, i) => i);
    const temp = new Array(n);

    function mergeSort(left, right) {
        if (left >= right) return;

        const mid = Math.floor((left + right) / 2);

        mergeSort(left, mid);
        mergeSort(mid + 1, right);

        let i = left;
        let j = mid + 1;
        let k = left;
        let smallerRight = 0;

        while (i <= mid && j <= right) {
            if (nums[indices[j]] < nums[indices[i]]) {
                temp[k++] = indices[j++];
                smallerRight++;
            } else {
                counts[indices[i]] += smallerRight;
                temp[k++] = indices[i++];
            }
        }

        while (i <= mid) {
            counts[indices[i]] += smallerRight;
            temp[k++] = indices[i++];
        }

        while (j <= right) {
            temp[k++] = indices[j++];
        }

        for (let p = left; p <= right; p++) {
            indices[p] = temp[p];
        }
    }

    mergeSort(0, n - 1);
    return counts;
};

