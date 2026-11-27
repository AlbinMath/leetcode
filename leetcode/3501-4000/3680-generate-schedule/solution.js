
var generateSchedule = function(n) {
    if (n < 5) return [];

    const matches = [];

    for (let i = 0; i < n; i++) {
        for (let j = 0; j < n; j++) {
            if (i !== j) {
                matches.push([i, j]);
            }
        }
    }

    const m = matches.length;
    const alive = new Uint8Array(m).fill(1);

    const degree = new Int32Array(m).fill((n - 2) * (n - 3));

    const schedule = [];
    let remaining = m;
    let current = -1;

    while (remaining > 0) {
        let best = -1;
        let bestDegree = Infinity;
        for (let i = 0; i < m; i++) {
            if (!alive[i]) continue;

            const [a, b] = matches[i];

            if (current !== -1) {
                const [p, q] = matches[current];

                if (a === p || a === q || b === p || b === q) {
                    continue;
                }
            }
            if (remaining > 1 && degree[i] === 0) {
                continue;
            }

            if (degree[i] < bestDegree) {
                bestDegree = degree[i];
                best = i;
            }
        }
        if (best === -1) {
            return [];
        }

        schedule.push(matches[best]);
        alive[best] = 0;
        remaining--;

        const [a, b] = matches[best];

        for (let i = 0; i < m; i++) {
            if (!alive[i]) continue;

            const [u, v] = matches[i];

            if (u !== a && u !== b && v !== a && v !== b) {
                degree[i]--;
            }
        }

        current = best;
    }

    return schedule;
};

