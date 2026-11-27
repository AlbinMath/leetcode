
var minPrice = function(prices, discounts) {
    prices.sort((a, b) => b - a);
    discounts.sort((a, b) => b - a);

    let total = 0;
    const limit = Math.min(prices.length, discounts.length);

    for (let i = 0; i < prices.length; i++) {
        if (i < limit) {
            total += prices[i] * (100 - discounts[i]) / 100;
        } else {
            total += prices[i];
        }
    }

    return total;
};

