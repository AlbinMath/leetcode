var minOperations = function(nums, k) {
    // Build a min-heap in-place (note: intermediate values can exceed 2^31 - 1, so use standard JS numbers)
    const heap = [...nums];
    const n = heap.length;

    const siftDown = (idx) => {
        const size = heap.length;
        while (true) {
            let smallest = idx;
            const left = (idx << 1) + 1;
            const right = left + 1;
            if (left < size && heap[left] < heap[smallest]) smallest = left;
            if (right < size && heap[right] < heap[smallest]) smallest = right;
            if (smallest === idx) break;
            [heap[idx], heap[smallest]] = [heap[smallest], heap[idx]];
            idx = smallest;
        }
    };

    const pop = () => {
        const top = heap[0];
        const last = heap.pop();
        if (heap.length > 0) {
            heap[0] = last;
            siftDown(0);
        }
        return top;
    };

    const push = (val) => {
        heap.push(val);
        let idx = heap.length - 1;
        while (idx > 0) {
            const parent = (idx - 1) >> 1;
            if (heap[idx] >= heap[parent]) break;
            [heap[idx], heap[parent]] = [heap[parent], heap[idx]];
            idx = parent;
        }
    };

    // Heapify in O(n)
    for (let i = (n >> 1) - 1; i >= 0; i--) {
        siftDown(i);
    }

    let operations = 0;
    while (heap.length >= 2 && heap[0] < k) {
        const x = pop();
        const y = pop();
        push(x * 2 + y);
        operations++;
    }

    return operations;
};
