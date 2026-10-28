/**
 * @param {number} n
 * @param {number} k
 * @return {number[]}
 */
var permute = function (n, k) {
    const fact = [1n];
    for (let i = 1; i <= n; i++) fact.push(fact[i - 1] * BigInt(i));

    let K = BigInt(k);
    const used = new Array(n + 1).fill(false);
    let ro = Math.ceil(n / 2); // odds remaining
    let re = Math.floor(n / 2); // evens remaining
    const res = [];

    for (let i = 0; i < n; i++) {
        let chosen = -1;
        for (let v = 1; v <= n; v++) {
            if (used[v]) continue;
            if (i > 0 && (v & 1) === (res[i - 1] & 1)) continue;

            // remaining counts after placing v
            const nro = ro - (v & 1);
            const nre = re - ((v & 1) ^ 1);
            const r = n - i - 1;
            // next position must have the opposite parity of v
            const nextIsOdd = (v & 1) === 0;
            const needOdd = nextIsOdd ? Math.ceil(r / 2) : Math.floor(r / 2);

            let cnt = 0n;
            if (nro >= 0 && nre >= 0 && needOdd === nro) {
                cnt = fact[nro] * fact[nre];
            }

            if (K > cnt) {
                K -= cnt;
            } else {
                chosen = v;
                break;
            }
        }
        if (chosen === -1) return [];
        used[chosen] = true;
        res.push(chosen);
        if (chosen & 1) ro--;
        else re--;
    }
    return res;
};
