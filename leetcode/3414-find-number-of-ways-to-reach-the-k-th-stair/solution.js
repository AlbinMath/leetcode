var waysToReachStair = function(k) {
    let ans = 0;

    function comb(n, r) {
        if (r < 0 || r > n) return 0;

        let res = 1;
        for (let i = 1; i <= r; i++) {
            res = res * (n - i + 1) / i;
        }
        return Math.round(res);
    }

    for (let j = 0; j <= 30; j++) {
        const pos = (1 << j);
        const downs = pos - k;

        if (downs >= 0 && downs <= j + 1) {
            ans += comb(j + 1, downs);
        }
    }

    return ans;
};
