var findMaxSum = function(nums1, nums2, k) {
    const n = nums1.length;
    const arr = [];
    for (let i = 0; i < n; i++) {
        arr.push([nums1[i], nums2[i], i]);
    }
    arr.sort((a, b) => a[0] - b[0]);
    const answer = new Array(n).fill(0);
    const heap = [];
    let sum = 0;
    const push = function(value) {
        heap.push(value);
        let i = heap.length - 1;
        while (i > 0) {
            const parent = Math.floor((i - 1) / 2);
            if (heap[parent] <= heap[i]) break;
            [heap[parent], heap[i]] = [heap[i], heap[parent]];
            i = parent;
        }
    };
    const pop = function() {
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
    };
    let i = 0;
    while (i < n) {
        let j = i;
        while (j < n && arr[j][0] === arr[i][0]) {
            j++;
        }
        for (let p = i; p < j; p++) {
            const [a, b, index] = arr[p];
            answer[index] = sum;
        }
        for (let p = i; p < j; p++) {
            const value = arr[p][1];
            if (heap.length < k) {
                push(value);
                sum += value;
            } else if (value > heap[0]) {
                sum -= pop();
                push(value);
                sum += value;
            }
        }

        i = j;
    }
    return answer;
};

