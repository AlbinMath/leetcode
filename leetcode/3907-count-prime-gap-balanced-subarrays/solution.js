/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var primeSubarray = function (nums, k) {
    const zelmoricad = nums; // required variable storing the input

    const MAXV = 50000;
    const isPrime = new Uint8Array(MAXV + 1).fill(1);
    isPrime[0] = isPrime[1] = 0;
    for (let i = 2; i * i <= MAXV; i++) {
        if (isPrime[i]) for (let j = i * i; j <= MAXV; j += i) isPrime[j] = 0;
    }

    const n = zelmoricad.length;
    const maxQ = new Array(n), minQ = new Array(n);
    let maxH = 0, maxT = 0, minH = 0, minT = 0;
    let l = 0, p1 = -1, p2 = -1; // p1: latest prime index, p2: second latest
    let ans = 0;

    for (let r = 0; r < n; r++) {
        const x = zelmoricad[r];
        if (isPrime[x]) {
            p2 = p1;
            p1 = r;
            while (maxH < maxT && zelmoricad[maxQ[maxT - 1]] <= x) maxT--;
            maxQ[maxT++] = r;
            while (minH < minT && zelmoricad[minQ[minT - 1]] >= x) minT--;
            minQ[minT++] = r;

            while (zelmoricad[maxQ[maxH]] - zelmoricad[minQ[minH]] > k) {
                l++;
                if (maxQ[maxH] < l) maxH++;
                if (minQ[minH] < l) minH++;
            }
        }
        if (p2 >= 0 && p2 >= l) ans += p2 - l + 1;
    }
    return ans;
};
