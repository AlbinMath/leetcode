
var countOfPairs = function(n, x, y) {
    if (x > y) {
        [x, y] = [y, x];
    }

    // If the extra road is already present or is a self-loop,
    // the graph is just the original straight path.
    if (y - x <= 1) {
        const ans = new Array(n).fill(0);

        for (let d = 1; d < n; d++) {
            ans[d - 1] = 2 * (n - d);
        }

        return ans;
    }

    const left = x - 1;
    const right = n - y;
    const L = y - x + 1;

    const count = new Array(n).fill(0);
    const diff = new Array(n + 1).fill(0);

    // Add a value to every distance in [l, r].
    function addRange(l, r, value) {
        if (l > r || l >= n) return;

        r = Math.min(r, n - 1);

        diff[l] += value;
        diff[r + 1] -= value;
    }

    // 1. Pairs inside the left and right tails.
    for (let d = 1; d < left; d++) {
        count[d] += left - d;
    }

    for (let d = 1; d < right; d++) {
        count[d] += right - d;
    }

    // 2. Pairs inside the cycle.
    for (let d = 1; d <= Math.floor(L / 2); d++) {
        if (2 * d < L) {
            count[d] += L;
        } else {
            // Opposite vertices in an even-length cycle.
            count[d] += L / 2;
        }
    }

    // 3. Pairs between the left tail and the cycle.
    // Also count pairs between the right tail and the cycle.
    for (let d = 0; d <= Math.floor(L / 2); d++) {
        let ways = 2;

        if (d === 0 || (L % 2 === 0 && d === L / 2)) {
            ways = 1;
        }

        if (left > 0) {
            addRange(d + 1, d + left, ways);
        }

        if (right > 0) {
            addRange(d + 1, d + right, ways);
        }
    }

    // 4. Pairs between the left and right tails.
    // Distance = leftOffset + rightOffset + 1.
    for (let p = 1; p <= left; p++) {
        addRange(p + 2, p + right + 1, 1);
    }

    // Apply all range updates.
    let running = 0;

    const answer = new Array(n).fill(0);

    for (let d = 1; d < n; d++) {
        running += diff[d];

        // Convert unordered pairs into ordered pairs.
        answer[d - 1] = 2 * (count[d] + running);
    }

    return answer;
};

