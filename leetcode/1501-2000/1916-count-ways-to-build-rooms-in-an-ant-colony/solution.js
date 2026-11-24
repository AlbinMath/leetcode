var waysToBuildRooms = function(prevRoom) {
    const MOD = 1000000007n;
    const n = prevRoom.length;

    const children = Array.from({ length: n }, () => []);

    for (let i = 1; i < n; i++) {
        children[prevRoom[i]].push(i);
    }

    const fact = Array(n + 1).fill(1n);
    const invFact = Array(n + 1).fill(1n);

    for (let i = 1; i <= n; i++) {
        fact[i] = fact[i - 1] * BigInt(i) % MOD;
    }

    function modPow(a, b) {
        let result = 1n;
        while (b > 0n) {
            if (b % 2n === 1n) result = result * a % MOD;
            a = a * a % MOD;
            b /= 2n;
        }
        return result;
    }

    invFact[n] = modPow(fact[n], MOD - 2n);

    for (let i = n; i >= 1; i--) {
        invFact[i - 1] = invFact[i] * BigInt(i) % MOD;
    }

    const size = Array(n).fill(1);
    const ways = Array(n).fill(1n);

    const order = [0];
    for (let i = 0; i < order.length; i++) {
        for (const child of children[order[i]]) {
            order.push(child);
        }
    }

    for (let i = n - 1; i >= 0; i--) {
        const node = order[i];
        let totalSize = 0;
        let result = 1n;

        for (const child of children[node]) {
            totalSize += size[child];
            result = result * ways[child] % MOD;
            result = result * invFact[size[child]] % MOD;
        }

        size[node] = totalSize + 1;
        ways[node] = result * fact[totalSize] % MOD;
    }

    return Number(ways[0]);
};
