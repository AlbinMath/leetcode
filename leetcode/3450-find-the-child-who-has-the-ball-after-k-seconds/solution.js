var numberOfChild = function(n, k) {
    const cycleLen = 2 * (n - 1);
    const rem = k % cycleLen;
    return rem <= n - 1 ? rem : cycleLen - rem;
};
