var maxScore = function(nums1, nums2, k) {
    const n = nums1.length;

    const pairs = [];

    for (let i = 0; i < n; i++) {
        pairs.push([nums1[i], nums2[i]]);
    }

    // Sort by nums2 in descending order
    pairs.sort((a, b) => b[1] - a[1]);

    // Min heap to keep the largest k nums1 values
    const heap = [];
    let sum = 0;
    let maxScore = 0;

    function push(val) {
        heap.push(val);
        let i = heap.length - 1;

        while (i > 0) {
            const parent = Math.floor((i - 1) / 2);

            if (heap[parent] <= heap[i]) break;

            [heap[parent], heap[i]] = [heap[i], heap[parent]];
            i = parent;
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
                const left = 2 * i + 1;
                const right = 2 * i + 2;

                if (
                    left < heap.length &&
                    heap[left] < heap[smallest]
                ) {
                    smallest = left;
                }

                if (
                    right < heap.length &&
                    heap[right] < heap[smallest]
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

    for (const [num1, num2] of pairs) {
        push(num1);
        sum += num1;

        if (heap.length > k) {
            sum -= pop();
        }

        if (heap.length === k) {
            maxScore = Math.max(maxScore, sum * num2);
        }
    }

    return maxScore;
};
