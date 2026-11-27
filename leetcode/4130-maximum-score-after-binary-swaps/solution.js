var maximumScore = function(nums, s) {
    const heap = [];
    let ans = 0;

    function push(value) {
        heap.push(value);

        let i = heap.length - 1;

        while (i > 0) {
            const parent = Math.floor((i - 1) / 2);

            if (heap[parent] >= heap[i]) break;

            [heap[parent], heap[i]] = [heap[i], heap[parent]];
            i = parent;
        }
    }

    function pop() {
        const max = heap[0];
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

        return max;
    }

    for (let i = 0; i < nums.length; i++) {
        push(nums[i]);

        if (s[i] === '1') {
            ans += pop();
        }
    }

    return ans;
};
