var getFinalState = function(nums, k, multiplier) {
    const n = nums.length;
    const heap = Array.from({ length: n }, (_, i) => i);

    const less = (a, b) =>
        nums[heap[a]] !== nums[heap[b]]
            ? nums[heap[a]] < nums[heap[b]]
            : heap[a] < heap[b];

    const siftDown = (idx) => {
        while (true) {
            let smallest = idx;
            const left = (idx << 1) + 1;
            const right = left + 1;
            if (left < n && less(left, smallest)) smallest = left;
            if (right < n && less(right, smallest)) smallest = right;
            if (smallest === idx) break;
            [heap[idx], heap[smallest]] = [heap[smallest], heap[idx]];
            idx = smallest;
        }
    };

    for (let i = (n >> 1) - 1; i >= 0; i--) {
        siftDown(i);
    }

    for (let op = 0; op < k; op++) {
        const minIdx = heap[0];
        nums[minIdx] *= multiplier;
        siftDown(0);
    }

    return nums;
};
