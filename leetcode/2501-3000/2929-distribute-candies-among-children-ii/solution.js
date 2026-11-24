var distributeCandies = function(n, limit) {
    const C2 = x => x < 2 ? 0 : x * (x - 1) / 2;

    return C2(n + 2)
         - 3 * C2(n - limit + 1)
         + 3 * C2(n - 2 * limit)
         - C2(n - 3 * limit - 1);
};
