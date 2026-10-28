var distributeCandies = function(n, limit) {
    let ways = 0;

    for (let a = 0; a <= Math.min(n, limit); a++) {
        for (let b = 0; b <= Math.min(n - a, limit); b++) {
            const c = n - a - b;

            if (c >= 0 && c <= limit) {
                ways++;
            }
        }
    }

    return ways;
};
