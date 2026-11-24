/**
 * @param {number[]} tasks
 * @param {number[]} workers
 * @param {number} pills
 * @param {number} strength
 * @return {number}
 */
var maxTaskAssign = function (tasks, workers, pills, strength) {
    tasks.sort((a, b) => a - b);
    workers.sort((a, b) => a - b);
    const n = tasks.length, m = workers.length;

    const check = (x) => {
        let p = pills;
        const dq = new Array(x);
        let head = 0, tail = 0;
        let ptr = 0; // next task (among the x easiest) to add to the deque

        for (let i = m - x; i < m; i++) {
            const w = workers[i];
            while (ptr < x && tasks[ptr] <= w + strength) {
                dq[tail++] = tasks[ptr++];
            }
            if (head === tail) return false;

            if (dq[head] <= w) {
                head++;                 // no pill needed, take the easiest
            } else {
                if (p === 0) return false;
                p--;
                tail--;                 // pill: take the hardest reachable
            }
        }
        return true;
    };

    let lo = 0, hi = Math.min(n, m);
    while (lo < hi) {
        const mid = (lo + hi + 1) >> 1;
        if (check(mid)) lo = mid;
        else hi = mid - 1;
    }
    return lo;
};
