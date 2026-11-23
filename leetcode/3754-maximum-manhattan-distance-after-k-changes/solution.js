var maxDistance = function(s, k) {
    let x = 0, y = 0;
    let maxDist = 0;

    for (let i = 0; i < s.length; i++) {
        switch (s[i]) {
            case 'N': y++; break;
            case 'S': y--; break;
            case 'E': x++; break;
            case 'W': x--; break;
        }

        // Maximum achievable distance at this prefix
        let dist = Math.abs(x) + Math.abs(y);
        let possible = Math.min(i + 1, dist + 2 * k);

        maxDist = Math.max(maxDist, possible);
    }

    return maxDist;
};
