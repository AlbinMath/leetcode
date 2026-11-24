/**
 * @param {string} stamp
 * @param {string} target
 * @return {number[]}
 */
var movesToStamp = function (stamp, target) {
    const m = stamp.length, n = target.length;
    const windows = n - m + 1;
    const t = target.split('');

    // todo[i]: set of positions in window i that still need to be blanked
    // (non-matching letters). Window is ready when todo is empty.
    const todoCount = new Array(windows).fill(0);
    const todoSets = new Array(windows);
    const queue = [];
    const visited = new Array(windows).fill(false);
    const blanked = new Array(n).fill(false);

    for (let i = 0; i < windows; i++) {
        const set = new Set();
        for (let j = 0; j < m; j++) {
            if (target[i + j] !== stamp[j]) set.add(i + j);
        }
        todoSets[i] = set;
        if (set.size === 0) {
            queue.push(i);
            visited[i] = true;
        }
    }

    const order = [];
    let head = 0;
    while (head < queue.length) {
        const i = queue[head++];
        order.push(i);
        for (let j = 0; j < m; j++) {
            const p = i + j;
            if (blanked[p]) continue;
            blanked[p] = true;
            // p is now a wildcard: remove it from every window covering it
            const lo = Math.max(0, p - m + 1);
            const hi = Math.min(windows - 1, p);
            for (let w = lo; w <= hi; w++) {
                if (visited[w]) continue;
                todoSets[w].delete(p);
                if (todoSets[w].size === 0) {
                    visited[w] = true;
                    queue.push(w);
                }
            }
        }
    }

    for (let p = 0; p < n; p++) {
        if (!blanked[p]) return [];
    }
    return order.reverse();
};
