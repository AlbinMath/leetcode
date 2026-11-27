
var maximumSaleItems = function(items, budget) {
    const n = items.length;

    const freq = new Array(n + 1).fill(0);

    let minPrice = Infinity;
    let maxFactor = 0;

    for (const [factor, price] of items) {
        freq[factor]++;
        minPrice = Math.min(minPrice, price);
        maxFactor = Math.max(maxFactor, factor);
    }

    const multiples = freq.slice();

    for (let f = 1; f <= maxFactor; f++) {
        for (let j = 2 * f; j <= maxFactor; j += f) {
            multiples[f] += freq[j];
        }
    }

    const offers = [];

    for (const [factor, price] of items) {
        const freeCount = multiples[factor] - 1;

        if (freeCount > 0 && price <= 2 * minPrice) {
            offers.push([price, freeCount]);
        }
    }

    offers.sort((a, b) => a[0] - b[0]);

    let answer = 0;

    for (const [price, count] of offers) {
        const take = Math.min(count, Math.floor(budget / price));

        answer += 2 * take;
        budget -= take * price;
    }

    answer += Math.floor(budget / minPrice);

    return answer;
};

