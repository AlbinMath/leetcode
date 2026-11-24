var isPossible = function(target) {
    let sum = target.reduce((a, b) => a + b, 0);
    const heap = [];

    function push(num) {
        heap.push(num);
        let i = heap.length - 1;

        while (i > 0) {
            let parent = Math.floor((i - 1) / 2);

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
                let left = 2 * i + 1;
                let right = 2 * i + 2;

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

        return max;
    }

    for (const num of target) {
        push(num);
    }

    while (true) {
        let largest = pop();
        let rest = sum - largest;

        if (largest === 1 || rest === 1) {
            return true;
        }

        if (rest === 0 || largest <= rest) {
            return false;
        }

        let previous = largest % rest;

        if (previous === 0) {
            return false;
        }

        sum = rest + previous;
        push(previous);
    }
};
