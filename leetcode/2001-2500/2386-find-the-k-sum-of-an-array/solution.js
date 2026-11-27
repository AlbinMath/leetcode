var kSum = function(nums, k) {
    let maxSum = 0;
    for (const num of nums) {
        if (num > 0) {
            maxSum += num;
        }
    }
    const arr = nums.map(Math.abs).sort((a, b) => a - b);
    const heap = [];
    const push = (item) => {
        heap.push(item);
        let i = heap.length - 1;
        while (i > 0) {
            const parent = Math.floor((i - 1) / 2);
            if (heap[parent][0] <= heap[i][0]) break;
            [heap[parent], heap[i]] = [heap[i], heap[parent]];
            i = parent;
        }
    };
    const pop = () => {
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
                    heap[left][0] < heap[smallest][0]
                ) {
                    smallest = left;
                }
                if (
                    right < heap.length &&
                    heap[right][0] < heap[smallest][0]
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
    push([0, -1]);
    let smallestSum = 0;
    for (let count = 0; count < k; count++) {
        const [sum, index] = pop();
        smallestSum = sum;
        const next = index + 1;
        if (next < arr.length) {
            push([sum + arr[next], next]);

            if (index >= 0) {
                push([
                    sum - arr[index] + arr[next],
                    next
                ]);
            }
        }
    }
    return maxSum - smallestSum;
};

