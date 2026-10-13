
var findMaximizedCapital = function(k, w, profits, capital) {
    const n = profits.length;

    // Sort projects by required capital
    const projects = [];

    for (let i = 0; i < n; i++) {
        projects.push([capital[i], profits[i]]);
    }

    projects.sort((a, b) => a[0] - b[0]);

    // Max heap storing available project profits
    const heap = [];

    function push(profit) {
        heap.push(profit);
        let i = heap.length - 1;

        while (i > 0) {
            const parent = Math.floor((i - 1) / 2);

            if (heap[parent] >= heap[i]) break;

            [heap[parent], heap[i]] = [heap[i], heap[parent]];
            i = parent;
        }
    }

    function pop() {
        if (heap.length === 1) return heap.pop();

        const maxProfit = heap[0];
        heap[0] = heap.pop();

        let i = 0;

        while (true) {
            let largest = i;
            const left = 2 * i + 1;
            const right = 2 * i + 2;

            if (
                left < heap.length &&
                heap[left] > heap[largest]
            ) {
                largest = left;
            }

            if (
                right < heap.length &&
                heap[right] > heap[largest]
            ) {
                largest = right;
            }

            if (largest === i) break;

            [heap[i], heap[largest]] =
                [heap[largest], heap[i]];

            i = largest;
        }

        return maxProfit;
    }

    let index = 0;

    for (let i = 0; i < k; i++) {
        // Add every project we can currently afford
        while (
            index < n &&
            projects[index][0] <= w
        ) {
            push(projects[index][1]);
            index++;
        }

        // No affordable projects remain
        if (heap.length === 0) break;

        // Choose the most profitable available project
        w += pop();
    }

    return w;
};

