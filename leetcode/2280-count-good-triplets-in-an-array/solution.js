
var goodTriplets = function(nums1, nums2) {
    const n = nums1.length;

    // Map each value to its position in nums2
    const pos = new Array(n);

    for (let i = 0; i < n; i++) {
        pos[nums2[i]] = i;
    }

    // Convert nums1 into positions in nums2
    const arr = nums1.map(value => pos[value]);

    // Fenwick Tree
    const bit = new Array(n + 1).fill(0);

    function update(index, value) {
        index++; // Convert to 1-based indexing

        while (index <= n) {
            bit[index] += value;
            index += index & -index;
        }
    }

    function query(index) {
        let sum = 0;
        index++; // Inclusive prefix sum

        while (index > 0) {
            sum += bit[index];
            index -= index & -index;
        }

        return sum;
    }

    let result = 0;

    for (let j = 0; j < n; j++) {
        // Number of earlier positions smaller than arr[j]
        const left = query(arr[j] - 1);

        // Number of later positions greater than arr[j]
        const right = (n - 1 - arr[j]) -
                      (j - left);

        result += left * right;

        // Insert current position for future elements
        update(arr[j], 1);
    }

    return result;
};

