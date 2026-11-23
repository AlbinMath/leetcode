var getFinalState = function(nums, k, multiplier) {
    const MOD = 1000000007n;
    const mult = BigInt(multiplier);
    const n = nums.length;

    if (multiplier === 1) {
        return nums.map((x) => Number(BigInt(x) % MOD));
    }

    const vals = nums.map((x) => BigInt(x));
    let maxVal = 0n;
    for (const v of vals) {
        if (v > maxVal) maxVal = v;
    }

    const heap = Array.from({ length: n }, (_, i) => i);

    const less = (a, b) =>
        vals[heap[a]] !== vals[heap[b]]
            ? vals[heap[a]] < vals[heap[b]]
            : heap[a] < heap[b];

    const siftDown = (idx) => {
        while (true) {
            let smallest = idx;
            const left = (idx << 1) + 1;
            const right = left + 1;
            if (left < heap.length && less(left, smallest)) smallest = left;
            if (right < heap.length && less(right, smallest)) smallest = right;
            if (smallest === idx) break;
            [heap[idx], heap[smallest]] = [heap[smallest], heap[idx]];
            idx = smallest;
        }
    };

    const pop = () => {
        const top = heap[0];
        const last = heap.pop();
        if (heap.length > 0) {
            heap[0] = last;
            siftDown(0);
        }
        return top;
    };

    const modPow = (base, exp) => {
        let res = 1n;
        base %= MOD;
        while (exp > 0n) {
            if (exp & 1n) res = (res * base) % MOD;
            base = (base * base) % MOD;
            exp >>= 1n;
        }
        return res;
    };

    for (let i = (n >> 1) - 1; i >= 0; i--) {
        siftDown(i);
    }

    // Phase 1: Simulate until the minimum value catches up to maxVal
    while (k > 0 && vals[heap[0]] < maxVal) {
        const minIdx = heap[0];
        vals[minIdx] *= mult;
        siftDown(0);
        k--;
    }

    // Phase 2: Distribute remaining k operations evenly across sorted heap order
    const kBig = BigInt(k);
    const nBig = BigInt(n);
    const baseExp = kBig / nBig;
    const rem = Number(kBig % nBig);
    const ans = new Array(n);

    for (let rank = 0; rank < n; rank++) {
        const idx = pop();
        const exp = baseExp + (rank < rem ? 1n : 0n);
        ans[idx] = Number(((vals[idx] % MOD) * modPow(mult, exp)) % MOD);
    }

    return ans;
};
