function smallestNumber(num: string, t: number): string {
    const primes = [2, 3, 5, 7];

    // Factorize t
    const need = [0, 0, 0, 0];

    for (let i = 0; i < 4; i++) {
        while (t % primes[i] === 0) {
            need[i]++;
            t /= primes[i];
        }
    }

    // t has a prime factor other than 2,3,5,7
    if (t !== 1) {
        return "-1";
    }

    // Prime factor contribution of digits 0..9
    const factors = [
        [0, 0, 0, 0], // 0
        [0, 0, 0, 0], // 1
        [1, 0, 0, 0], // 2
        [0, 1, 0, 0], // 3
        [2, 0, 0, 0], // 4
        [0, 0, 1, 0], // 5
        [1, 1, 0, 0], // 6
        [0, 0, 0, 1], // 7
        [3, 0, 0, 0], // 8
        [0, 2, 0, 0]  // 9
    ];

    const A = need[0] + 1;
    const B = need[1] + 1;
    const C = need[2] + 1;
    const D = need[3] + 1;

    const size = A * B * C * D;

    const getId = (
        a: number,
        b: number,
        c: number,
        d: number
    ): number => {
        return (((a * B) + b) * C + c) * D + d;
    };

    /*
     * dp[a,b,c,d] =
     * minimum number of digits needed to provide
     * at least a factors of 2,
     * at least b factors of 3,
     * at least c factors of 5,
     * at least d factors of 7.
     */
    const dp = new Uint8Array(size);
    dp.fill(255);

    dp[0] = 0;

    // Iterative DP — no recursion
    for (let a = 0; a <= need[0]; a++) {
        for (let b = 0; b <= need[1]; b++) {
            for (let c = 0; c <= need[2]; c++) {
                for (let d = 0; d <= need[3]; d++) {

                    if (a === 0 && b === 0 && c === 0 && d === 0) {
                        continue;
                    }

                    let best = 255;

                    for (let digit = 2; digit <= 9; digit++) {
                        const f = factors[digit];

                        const na = Math.max(0, a - f[0]);
                        const nb = Math.max(0, b - f[1]);
                        const nc = Math.max(0, c - f[2]);
                        const nd = Math.max(0, d - f[3]);

                        const prev = dp[getId(na, nb, nc, nd)];

                        if (prev !== 255) {
                            best = Math.min(best, prev + 1);
                        }
                    }

                    dp[getId(a, b, c, d)] = best;
                }
            }
        }
    }

    const minDigits = (
        a: number,
        b: number,
        c: number,
        d: number
    ): number => {
        return dp[getId(a, b, c, d)];
    };

    // Factor contribution after adding a digit
    const subtract = (
        req: number[],
        digit: number
    ): number[] => {
        const f = factors[digit];

        return [
            Math.max(0, req[0] - f[0]),
            Math.max(0, req[1] - f[1]),
            Math.max(0, req[2] - f[2]),
            Math.max(0, req[3] - f[3])
        ];
    };

    /*
     * Construct the lexicographically smallest
     * zero-free number of exactly `length` digits
     * satisfying the required factors.
     */
    const buildSmallest = (
        length: number,
        initialReq: number[]
    ): string => {
        const result: string[] = [];
        let req = [...initialReq];

        for (let pos = 0; pos < length; pos++) {
            const remaining = length - pos - 1;

            for (let digit = 1; digit <= 9; digit++) {
                const next = subtract(req, digit);

                if (
                    minDigits(
                        next[0],
                        next[1],
                        next[2],
                        next[3]
                    ) <= remaining
                ) {
                    result.push(String(digit));
                    req = next;
                    break;
                }
            }
        }

        return result.join("");
    };

    /*
     * Check whether num itself already works.
     */
    let cur = [0, 0, 0, 0];
    let hasZero = false;

    for (const ch of num) {
        const digit = Number(ch);

        if (digit === 0) {
            hasZero = true;
            continue;
        }

        const f = factors[digit];

        for (let j = 0; j < 4; j++) {
            cur[j] = Math.min(
                need[j],
                cur[j] + f[j]
            );
        }
    }

    if (
        !hasZero &&
        cur[0] >= need[0] &&
        cur[1] >= need[1] &&
        cur[2] >= need[2] &&
        cur[3] >= need[3]
    ) {
        return num;
    }

    const n = num.length;

    /*
     * Prefix factor counts.
     */
    const p2 = new Int32Array(n + 1);
    const p3 = new Int32Array(n + 1);
    const p5 = new Int32Array(n + 1);
    const p7 = new Int32Array(n + 1);

    const prefixHasZero = new Uint8Array(n + 1);

    for (let i = 0; i < n; i++) {
        const digit = Number(num[i]);
        const f = factors[digit];

        p2[i + 1] = Math.min(
            need[0],
            p2[i] + f[0]
        );

        p3[i + 1] = Math.min(
            need[1],
            p3[i] + f[1]
        );

        p5[i + 1] = Math.min(
            need[2],
            p5[i] + f[2]
        );

        p7[i + 1] = Math.min(
            need[3],
            p7[i] + f[3]
        );

        prefixHasZero[i + 1] =
            prefixHasZero[i] || digit === 0 ? 1 : 0;
    }

    /*
     * Try to construct a number with the SAME length
     * that is strictly greater than num.
     *
     * Change the rightmost possible position.
     */
    for (let i = n - 1; i >= 0; i--) {

        // Prefix cannot contain zero.
        if (prefixHasZero[i]) {
            continue;
        }

        const currentDigit = Number(num[i]);

        const req = [
            Math.max(0, need[0] - p2[i]),
            Math.max(0, need[1] - p3[i]),
            Math.max(0, need[2] - p5[i]),
            Math.max(0, need[3] - p7[i])
        ];

        for (let digit = currentDigit + 1; digit <= 9; digit++) {

            const next = subtract(req, digit);
            const remaining = n - i - 1;

            if (
                minDigits(
                    next[0],
                    next[1],
                    next[2],
                    next[3]
                ) <= remaining
            ) {
                return (
                    num.substring(0, i) +
                    digit.toString() +
                    buildSmallest(remaining, next)
                );
            }
        }
    }

    /*
     * No valid number with the same length.
     * Therefore use the smallest possible longer length.
     */
    const requiredLength = minDigits(
        need[0],
        need[1],
        need[2],
        need[3]
    );

    const length = Math.max(n + 1, requiredLength);

    return buildSmallest(length, [...need]);
}
