
var numberOfPairs = function(nums1, nums2, diff) {
    const n = nums1.length;
    const arr = new Array(n);

    for (let i = 0; i < n; i++) {
        arr[i] = nums1[i] - nums2[i];
    }

    const temp = new Array(n);

    function mergeSort(left, right) {
        if (left >= right) return 0;

        const mid = Math.floor((left + right) / 2);

        let count = mergeSort(left, mid);
        count += mergeSort(mid + 1, right);

        // Count valid pairs across the two halves
        let j = mid + 1;

        for (let i = left; i <= mid; i++) {
            while (
                j <= right &&
                arr[i] > arr[j] + diff
            ) {
                j++;
            }

            count += right - j + 1;
        }

        // Merge the sorted halves
        let i = left;
        j = mid + 1;
        let k = left;

        while (i <= mid && j <= right) {
            if (arr[i] <= arr[j]) {
                temp[k++] = arr[i++];
            } else {
                temp[k++] = arr[j++];
            }
        }

        while (i <= mid) {
            temp[k++] = arr[i++];
        }

        while (j <= right) {
            temp[k++] = arr[j++];
        }

        for (let p = left; p <= right; p++) {
            arr[p] = temp[p];
        }

        return count;
    }

    return mergeSort(0, n - 1);
};

