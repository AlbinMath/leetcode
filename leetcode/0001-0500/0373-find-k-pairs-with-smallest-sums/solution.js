var kSmallestPairs = function(nums1, nums2, k) {
    const result = [];
    const heap = [];

    function push(node) {
        heap.push(node);
        let i = heap.length - 1;

        while (i > 0) {
            let p = Math.floor((i - 1) / 2);

            if (heap[p].sum <= heap[i].sum) break;

            [heap[p], heap[i]] = [heap[i], heap[p]];
            i = p;
        }
    }

    function pop() {
        const min = heap[0];
        const last = heap.pop();

        if (heap.length > 0) {
            heap[0] = last;
            let i = 0;

            while (true) {
                let smallest = i;
                let left = 2 * i + 1;
                let right = 2 * i + 2;

                if (
                    left < heap.length &&
                    heap[left].sum < heap[smallest].sum
                ) {
                    smallest = left;
                }

                if (
                    right < heap.length &&
                    heap[right].sum < heap[smallest].sum
                ) {
                    smallest = right;
                }

                if (smallest === i) break;

                [heap[i], heap[smallest]] =
                    [heap[smallest], heap[i]];

                i = smallest;
            }
        }

        return min;
    }

    // Initialize the heap with the first pair from each row.
    for (let i = 0; i < Math.min(nums1.length, k); i++) {
        push({
            i: i,
            j: 0,
            sum: nums1[i] + nums2[0]
        });
    }

    while (result.length < k && heap.length > 0) {
        const current = pop();
        const { i, j } = current;

        result.push([nums1[i], nums2[j]]);

        // Add the next pair from the same row.
        if (j + 1 < nums2.length) {
            push({
                i: i,
                j: j + 1,
                sum: nums1[i] + nums2[j + 1]
            });
        }
    }

    return result;
};
