var circularGameLosers = function(n, k) {
    const visited = new Uint8Array(n);
    let curr = 0;
    let step = 1;

    while (!visited[curr]) {
        visited[curr] = 1;
        curr = (curr + step * k) % n;
        step++;
    }

    const losers = [];
    for (let i = 0; i < n; i++) {
        if (!visited[i]) {
            losers.push(i + 1);
        }
    }

    return losers;
};
