
var numberOfAlternatingGroups = function(colors, queries) {
    const n = colors.length;

    // Fenwick tree for the positions of equal-adjacent edges.
    const posBIT = new Array(n + 1).fill(0);

    // Fenwick trees for gap lengths and weighted gap lengths.
    const countBIT = new Array(n + 1).fill(0);
    const sumBIT = new Array(n + 1).fill(0);

    const isBreak = new Array(n).fill(false);
    let breakCount = 0;

    function posAdd(index, delta) {
        for (let i = index + 1; i <= n; i += i & -i) {
            posBIT[i] += delta;
        }
    }

    // Count break positions in [0, end).
    function posPrefix(end) {
        let result = 0;

        for (let i = end; i > 0; i -= i & -i) {
            result += posBIT[i];
        }

        return result;
    }

    // Return the zero-based position of the kth break (1-indexed k).
    function kth(k) {
        let index = 0;
        let step = 1;

        while (step * 2 <= n) step *= 2;

        for (; step > 0; step = Math.floor(step / 2)) {
            const next = index + step;

            if (next <= n && posBIT[next] < k) {
                index = next;
                k -= posBIT[next];
            }
        }

        return index;
    }

    function gapLength(a, b) {
        const d = (b - a + n) % n;
        return d === 0 ? n : d;
    }

    function gapAdd(length, delta) {
        for (let i = length; i <= n; i += i & -i) {
            countBIT[i] += delta;
            sumBIT[i] += length * delta;
        }
    }

    function gapPrefix(bit, index) {
        let result = 0;

        for (let i = index; i > 0; i -= i & -i) {
            result += bit[i];
        }

        return result;
    }

    function addBreak(x) {
        if (isBreak[x]) return;

        if (breakCount === 0) {
            gapAdd(n, 1);
        } else {
            const less = posPrefix(x);
            const p = less === 0 ? kth(breakCount) : kth(less);

            const le = posPrefix(x + 1);
            const s = le === breakCount ? kth(1) : kth(le + 1);

            gapAdd(gapLength(p, s), -1);
            gapAdd(gapLength(p, x), 1);
            gapAdd(gapLength(x, s), 1);
        }

        posAdd(x, 1);
        isBreak[x] = true;
        breakCount++;
    }

    function removeBreak(x) {
        if (!isBreak[x]) return;

        if (breakCount === 1) {
            gapAdd(n, -1);
        } else {
            const less = posPrefix(x);
            const p = less === 0 ? kth(breakCount) : kth(less);

            const s = less + 2 > breakCount
                ? kth(1)
                : kth(less + 2);

            gapAdd(gapLength(p, x), -1);
            gapAdd(gapLength(x, s), -1);
            gapAdd(gapLength(p, s), 1);
        }

        posAdd(x, -1);
        isBreak[x] = false;
        breakCount--;
    }

    // Initialize equal-adjacent edges, including the circular edge.
    for (let i = 0; i < n; i++) {
        if (colors[i] === colors[(i + 1) % n]) {
            addBreak(i);
        }
    }

    const answer = [];

    for (const query of queries) {
        if (query[0] === 1) {
            const k = query[1];

            if (breakCount === 0) {
                answer.push(n);
                continue;
            }

            const smallCount = gapPrefix(countBIT, k - 1);
            const smallSum = gapPrefix(sumBIT, k - 1);

            const totalCount = gapPrefix(countBIT, n);
            const totalSum = gapPrefix(sumBIT, n);

            const count = totalCount - smallCount;
            const sum = totalSum - smallSum;

            answer.push(sum - (k - 1) * count);
        } else {
            const index = query[1];
            const color = query[2];

            if (colors[index] === color) continue;

            const leftEdge = (index - 1 + n) % n;
            const rightEdge = index;

            removeBreak(leftEdge);
            removeBreak(rightEdge);

            colors[index] = color;

            if (colors[leftEdge] === colors[index]) {
                addBreak(leftEdge);
            }

            if (colors[index] === colors[(index + 1) % n]) {
                addBreak(rightEdge);
            }
        }
    }

    return answer;
};

