/**
 * @param {number[][]} points
 * @param {number} k
 * @return {number}
 */
var findMaxValueOfEquation = function (points, k) {
    const n = points.length;
    const dq = new Array(n);
    let head = 0, tail = 0; // deque occupies dq[head..tail-1]
    let ans = -Infinity;

    for (let j = 0; j < n; j++) {
        const [xj, yj] = points[j];

        while (head < tail && xj - points[dq[head]][0] > k) head++;

        if (head < tail) {
            const [xi, yi] = points[dq[head]];
            ans = Math.max(ans, (yi - xi) + (yj + xj));
        }

        const val = yj - xj;
        while (head < tail) {
            const [xb, yb] = points[dq[tail - 1]];
            if (yb - xb <= val) tail--;
            else break;
        }
        dq[tail++] = j;
    }
    return ans;
};
