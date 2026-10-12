var totalCost = function(costs, k, candidates) {
    const n = costs.length;
    let total = 0;
    let left = 0;
    let right = n - 1;

    const leftHeap = [];
    const rightHeap = [];

    function push(heap, worker) {
        heap.push(worker);
        let i = heap.length - 1;

        while (i > 0) {
            const parent = Math.floor((i - 1) / 2);

            if (
                heap[parent][0] < heap[i][0] ||
                (heap[parent][0] === heap[i][0] &&
                 heap[parent][1] < heap[i][1])
            ) {
                break;
            }

            [heap[parent], heap[i]] = [heap[i], heap[parent]];
            i = parent;
        }
    }

    function pop(heap) {
        const min = heap[0];
        const last = heap.pop();

        if (heap.length > 0) {
            heap[0] = last;
            let i = 0;

            while (true) {
                let smallest = i;
                const l = 2 * i + 1;
                const r = 2 * i + 2;

                function isSmaller(a, b) {
                    return (
                        heap[a][0] < heap[b][0] ||
                        (heap[a][0] === heap[b][0] &&
                         heap[a][1] < heap[b][1])
                    );
                }

                if (l < heap.length && isSmaller(l, smallest)) {
                    smallest = l;
                }

                if (r < heap.length && isSmaller(r, smallest)) {
                    smallest = r;
                }

                if (smallest === i) break;

                [heap[i], heap[smallest]] =
                    [heap[smallest], heap[i]];

                i = smallest;
            }
        }

        return min;
    }

    // Fill the initial candidate heaps
    while (leftHeap.length < candidates && left <= right) {
        push(leftHeap, [costs[left], left]);
        left++;
    }

    while (rightHeap.length < candidates && left <= right) {
        push(rightHeap, [costs[right], right]);
        right--;
    }

    // Hire k workers
    for (let i = 0; i < k; i++) {
        if (
            rightHeap.length === 0 ||
            (leftHeap.length > 0 &&
             (leftHeap[0][0] < rightHeap[0][0] ||
              (leftHeap[0][0] === rightHeap[0][0] &&
               leftHeap[0][1] < rightHeap[0][1])))
        ) {
            const [cost] = pop(leftHeap);
            total += cost;

            if (left <= right) {
                push(leftHeap, [costs[left], left]);
                left++;
            }
        } else {
            const [cost] = pop(rightHeap);
            total += cost;

            if (left <= right) {
                push(rightHeap, [costs[right], right]);
                right--;
            }
        }
    }

    return total;
};
