
var getSkyline = function(buildings) {
    const events = [];

    for (const [left, right, height] of buildings) {
        events.push([left, -height]);
        events.push([right, height]);
    }

    events.sort((a, b) => a[0] - b[0] || a[1] - b[1]);

    const result = [];
    const heap = [0];
    const active = new Map([[0, 1]]);

    function push(height) {
        heap.push(height);
        let i = heap.length - 1;

        while (i > 0) {
            const parent = Math.floor((i - 1) / 2);

            if (heap[parent] >= heap[i]) break;

            [heap[parent], heap[i]] = [heap[i], heap[parent]];
            i = parent;
        }
    }

    function pop() {
        const top = heap[0];
        const last = heap.pop();

        if (heap.length > 0) {
            heap[0] = last;
            let i = 0;

            while (true) {
                let largest = i;
                const left = 2 * i + 1;
                const right = 2 * i + 2;

                if (left < heap.length &&
                    heap[left] > heap[largest]) {
                    largest = left;
                }

                if (right < heap.length &&
                    heap[right] > heap[largest]) {
                    largest = right;
                }

                if (largest === i) break;

                [heap[i], heap[largest]] =
                    [heap[largest], heap[i]];

                i = largest;
            }
        }

        return top;
    }

    let prevMax = 0;
    let i = 0;

    while (i < events.length) {
        const x = events[i][0];

        // Process every event at this x-coordinate.
        while (i < events.length && events[i][0] === x) {
            const h = events[i][1];
            const height = Math.abs(h);

            if (h < 0) {
                active.set(height, (active.get(height) || 0) + 1);
                push(height);
            } else {
                active.set(height, (active.get(height) || 0) - 1);
            }

            i++;
        }

        // Remove expired heights from the top.
        while (
            heap.length > 0 &&
            (active.get(heap[0]) || 0) === 0
        ) {
            pop();
        }

        const currentMax = heap[0] || 0;

        if (currentMax !== prevMax) {
            result.push([x, currentMax]);
            prevMax = currentMax;
        }
    }

    return result;
};

