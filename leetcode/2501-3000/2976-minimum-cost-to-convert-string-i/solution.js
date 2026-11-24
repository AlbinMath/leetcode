
var minimumCost = function (source, target, original, changed, cost) {
    const INF = Infinity;
    const dist = Array.from({ length: 26 }, (_, i) => {
        const row = new Array(26).fill(INF);
        row[i] = 0;
        return row;
    });

    for (let i = 0; i < cost.length; i++) {
        const a = original[i].charCodeAt(0) - 97;
        const b = changed[i].charCodeAt(0) - 97;
        if (cost[i] < dist[a][b]) dist[a][b] = cost[i];
    }

    for (let k = 0; k < 26; k++) {
        for (let i = 0; i < 26; i++) {
            if (dist[i][k] === INF) continue;
            for (let j = 0; j < 26; j++) {
                const d = dist[i][k] + dist[k][j];
                if (d < dist[i][j]) dist[i][j] = d;
            }
        }
    }

    let total = 0;
    for (let i = 0; i < source.length; i++) {
        const d = dist[source.charCodeAt(i) - 97][target.charCodeAt(i) - 97];
        if (d === INF) return -1;
        total += d;
    }
    return total;
};
