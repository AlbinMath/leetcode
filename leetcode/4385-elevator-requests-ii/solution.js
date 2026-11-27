var elevatorRequests = function(n, start, requests) {
    const m = requests.length;
    const positions = [...requests];
    if (!positions.includes(start)) {
        positions.push(start);
    }
    positions.sort((a, b) => a - b);
    const N = positions.length;
    const s = positions.indexOf(start);
    const isRequest = new Array(N).fill(0);
    const requestSet = new Set(requests);
    for (let i = 0; i < N; i++) {
        if (requestSet.has(positions[i])) {
            isRequest[i] = 1;
        }
    }
    const prefix = new Array(N + 1).fill(0);
    for (let i = 0; i < N; i++) {
        prefix[i + 1] = prefix[i] + isRequest[i];
    }
    const size = N * N;
    const dpL = new Float64Array(size);
    const dpR = new Float64Array(size);
    dpL.fill(Infinity);
    dpR.fill(Infinity);
    const index = (l, r) => l * N + r;
    dpL[index(s, s)] = 0;
    dpR[index(s, s)] = 0;
    for (let l = s; l >= 0; l--) {
        for (let r = s; r < N; r++) {
            const idx = index(l, r);
            const leftCost = dpL[idx];
            const rightCost = dpR[idx];
            const fulfilled = prefix[r + 1] - prefix[l];
            const remaining = m - fulfilled;
            if (l > 0) {
                const nextIdx = index(l - 1, r);
                dpL[nextIdx] = Math.min(
                    dpL[nextIdx],
                    leftCost +
                        (positions[l] - positions[l - 1]) * remaining,
                    rightCost +
                        (positions[r] - positions[l - 1]) * remaining
                );
            }
            if (r < N - 1) {
                const nextIdx = index(l, r + 1);
                dpR[nextIdx] = Math.min(
                    dpR[nextIdx],
                    leftCost +
                        (positions[r + 1] - positions[l]) * remaining,
                    rightCost +
                        (positions[r + 1] - positions[r]) * remaining
                );
            }
        }
    }
    const finalIdx = index(0, N - 1);
    return Math.min(dpL[finalIdx], dpR[finalIdx]);
};

