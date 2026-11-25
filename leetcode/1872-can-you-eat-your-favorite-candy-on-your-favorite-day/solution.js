
var canEat = function(candiesCount, queries) {
    const n = candiesCount.length;

    // Build prefix sum
    let prefix = new Array(n);
    prefix[0] = candiesCount[0];

    for (let i = 1; i < n; i++) {
        prefix[i] = prefix[i - 1] + candiesCount[i];
    }

    let answer = [];

    for (let [type, day, cap] of queries) {
        let before = type === 0 ? 0 : prefix[type - 1];
        let through = prefix[type];
        let minEaten = day + 1;
        let maxEaten = BigInt(day + 1) * BigInt(cap);

        let canEatFavorite =
            minEaten <= through &&
            maxEaten > BigInt(before);

        answer.push(canEatFavorite);
    }

    return answer;
};

