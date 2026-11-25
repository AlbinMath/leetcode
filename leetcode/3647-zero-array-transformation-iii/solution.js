var maxRemoval = function(nums, queries) {
    const n = nums.length;
    const q = queries.length;
    queries.sort((a, b) => a[0] - b[0]);
    const heap = [];
    function push(val) {
        heap.push(val);
        let i = heap.length - 1;
        while (i > 0) {
            const parent = Math.floor((i - 1) / 2);
            if (heap[parent] >= heap[i]) break;
            [heap[parent], heap[i]] = [heap[i], heap[parent]];
            i = parent;
        }
    }
    function pop() {
        const result = heap[0];
        const last = heap.pop();
        if (heap.length > 0) {
            heap[0] = last;
            let i = 0;
            while (true) {
                let largest = i;
                const left = 2 * i + 1;
                const right = 2 * i + 2;

                if (left < heap.length && heap[left] > heap[largest]) {
                    largest = left;
                }
                if (right < heap.length && heap[right] > heap[largest]) {
                    largest = right;
                }
                if (largest === i) break;
                [heap[i], heap[largest]] = [heap[largest], heap[i]];
                i = largest;
            }
        }
        return result;
    }
    const diff = new Array(n + 1).fill(0);
    let active = 0;
    let j = 0;
    let selected = 0;
    for (let i = 0; i < n; i++) {
        active += diff[i];
        while (j < q && queries[j][0] <= i) {
            push(queries[j][1]);
            j++;
        }
        while (active < nums[i]) {
            while (heap.length > 0 && heap[0] < i) {
                pop();
            }
            if (heap.length === 0) {
                return -1;
            }
            const r = pop();
            active++;
            selected++;
            diff[r + 1]--;
        }
    }
    return q - selected;
};

