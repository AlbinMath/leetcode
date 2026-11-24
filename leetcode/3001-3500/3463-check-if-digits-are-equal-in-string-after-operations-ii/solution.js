/**
 * @param {string} s
 * @return {boolean}
 */
var hasSameDigits = function (s) {
    const n = s.length;
    const L = n - 2;

    // Pascal's triangle mod 5 for digits 0..4
    const C5 = [
        [1],
        [1, 1],
        [1, 2, 1],
        [1, 3, 3, 1],
        [1, 4, 1, 4, 1], // 1,4,6,4,1 mod 5
    ];

    const lucas5 = (a, b) => {
        let r = 1;
        while (a > 0 || b > 0) {
            const x = a % 5, y = b % 5;
            if (y > x) return 0;
            r = (r * C5[x][y]) % 5;
            a = Math.floor(a / 5);
            b = Math.floor(b / 5);
        }
        return r;
    };

    let sum2 = 0, sum5 = 0;
    for (let i = 0; i <= L; i++) {
        const d = s.charCodeAt(i + 1) - s.charCodeAt(i);

        if ((i & L) === i) sum2 += d;
        sum5 += lucas5(L, i) * d;
    }

    const mod2 = ((sum2 % 2) + 2) % 2;
    const mod5 = ((sum5 % 5) + 5) % 5;
    return mod2 === 0 && mod5 === 0;
};
