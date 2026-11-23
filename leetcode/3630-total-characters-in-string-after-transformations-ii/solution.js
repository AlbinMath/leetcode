var lengthAfterTransformations = function(s, t, nums) {
    const MOD = 1000000007n;
    const n = 26;

    // Initial frequency
    let freq = Array(n).fill(0n);

    for (const ch of s) {
        freq[ch.charCodeAt(0) - 97]++;
    }

    // Build transformation matrix
    let M = Array.from({ length: n }, () => Array(n).fill(0n));

    for (let j = 0; j < n; j++) {
        for (let k = 1; k <= nums[j]; k++) {
            let d = (j + k) % n;
            M[d][j] = 1n;
        }
    }

    // Matrix multiplication
    function multiply(A, B) {
        let C = Array.from({ length: n }, () => Array(n).fill(0n));

        for (let i = 0; i < n; i++) {
            for (let k = 0; k < n; k++) {
                if (A[i][k] === 0n) continue;

                for (let j = 0; j < n; j++) {
                    if (B[k][j] === 0n) continue;

                    C[i][j] = (
                        C[i][j] + A[i][k] * B[k][j]
                    ) % MOD;
                }
            }
        }

        return C;
    }

    // Matrix-vector multiplication
    function multiplyVector(A, v) {
        let result = Array(n).fill(0n);

        for (let i = 0; i < n; i++) {
            for (let j = 0; j < n; j++) {
                result[i] = (
                    result[i] + A[i][j] * v[j]
                ) % MOD;
            }
        }

        return result;
    }

    // Binary exponentiation
    while (t > 0) {
        if (t % 2 === 1) {
            freq = multiplyVector(M, freq);
        }

        M = multiply(M, M);
        t = Math.floor(t / 2);
    }

    // Final length
    let ans = 0n;

    for (const x of freq) {
        ans = (ans + x) % MOD;
    }

    return Number(ans);
};
