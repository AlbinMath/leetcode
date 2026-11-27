var getOrder = function(tasks) {
    const n = tasks.length;
    const sortedTasks = tasks.map((task, index) => [
        task[0],
        task[1],
        index
    ]);
    sortedTasks.sort((a, b) => a[0] - b[0]);
    const heap = [];
    const compare = (a, b) => {
        if (a[0] !== b[0]) {
            return a[0] - b[0];
        }
        return a[1] - b[1];
    };
    const push = (value) => {
        heap.push(value);
        let i = heap.length - 1;
        while (i > 0) {
            const parent = Math.floor((i - 1) / 2);
            if (compare(heap[parent], heap[i]) <= 0) {
                break;
            }
            [heap[parent], heap[i]] = [heap[i], heap[parent]];
            i = parent;
        }
    };
    const pop = () => {
        if (heap.length === 0) return null;
        const result = heap[0];
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
                    compare(heap[left], heap[smallest]) < 0
                ) {
                    smallest = left;
                }
                if (
                    right < heap.length &&
                    compare(heap[right], heap[smallest]) < 0
                ) {
                    smallest = right;
                }
                if (smallest === i) break;
                [heap[i], heap[smallest]] =
                    [heap[smallest], heap[i]];
                i = smallest;
            }
        }
        return result;
    };
    const result = [];
    let time = 0;
    let i = 0;
    while (i < n || heap.length > 0) {
        if (heap.length === 0 && time < sortedTasks[i][0]) {
            time = sortedTasks[i][0];
        }
        while (i < n && sortedTasks[i][0] <= time) {
            const [enqueueTime, processingTime, index] = sortedTasks[i];
            push([processingTime, index]);
            i++;
        }
        const [processingTime, index] = pop();
        result.push(index);
        time += processingTime;
    }
    return result;
};

