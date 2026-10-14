
var leftmostBuildingQueries = function(heights, queries) {
    const n = heights.length;
    const ans = new Array(queries.length).fill(-1);
    const waiting = Array.from({ length: n }, () => []);

    for (let i = 0; i < queries.length; i++) {
        let [a, b] = queries[i];

        if (a > b) [a, b] = [b, a];

        if (a === b || heights[a] < heights[b]) {
            ans[i] = b;
        } else {
            waiting[b].push([heights[a], i]);
        }
    }

    const heap = [];

    function push(item) {
        heap.push(item);
        let i = heap.length - 1;

        while (i > 0) {
            const p = Math.floor((i - 1) / 2);
            if (heap[p][0] <= heap[i][0]) break;

            [heap[p], heap[i]] = [heap[i], heap[p]];
            i = p;
        }
    }

    function pop() {
        const result = heap[0];
        const last = heap.pop();

        if (heap.length > 0) {
            heap[0] = last;
            let i = 0;

            while (true) {
                let smallest = i;
                const l = 2 * i + 1;
                const r = 2 * i + 2;

                if (l < heap.length &&
                    heap[l][0] < heap[smallest][0]) {
                    smallest = l;
                }

                if (r < heap.length &&
                    heap[r][0] < heap[smallest][0]) {
                    smallest = r;
                }

                if (smallest === i) break;

                [heap[i], heap[smallest]] =
                    [heap[smallest], heap[i]];

                i = smallest;
            }
        }

        return result;
    }

    for (let i = 0; i < n; i++) {
        while (heap.length > 0 && heap[0][0] < heights[i]) {
            const [, queryIndex] = pop();
            ans[queryIndex] = i;
        }

        for (const item of waiting[i]) {
            push(item);
        }
    }

    return ans;
};

