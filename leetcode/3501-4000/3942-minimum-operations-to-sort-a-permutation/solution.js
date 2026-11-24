/**
 * @param {number[]} nums
 * @return {number}
 */
var minOperations = function(nums) {
    const n = nums.length;
    const pos = nums.indexOf(0);
    let ans = Infinity;

    // Check if nums is a rotation of sorted order.
    let forward = true;

    for (let i = 0; i < n; i++) {
        if (nums[(pos + i) % n] !== i) {
            forward = false;
            break;
        }
    }

    if (forward) {
        // Rotate left directly.
        ans = Math.min(ans, pos);

        // Reverse, rotate left, reverse.
        if (pos > 0) {
            ans = Math.min(ans, n - pos + 2);
        }
    }

    // Check if nums is a rotation of reverse sorted order.
    let backward = true;

    for (let i = 0; i < n; i++) {
        if (nums[(pos - i + n) % n] !== i) {
            backward = false;
            break;
        }
    }

    if (backward) {
        // Reverse first, then rotate left.
        ans = Math.min(ans, n - 1 - pos + 1);

        // Rotate left first, then reverse.
        ans = Math.min(ans, (pos + 1) % n + 1);
    }

    return ans === Infinity ? -1 : ans;
};
