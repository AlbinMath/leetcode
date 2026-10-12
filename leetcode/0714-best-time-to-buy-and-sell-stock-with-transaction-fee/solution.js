var maxProfit = function(prices, fee) {
    let cash = 0;
    let hold = -prices[0];

    for (let i = 1; i < prices.length; i++) {
        const prevCash = cash;
        const prevHold = hold;

        // Maximum profit without holding a stock
        cash = Math.max(
            prevCash,
            prevHold + prices[i] - fee
        );

        // Maximum profit while holding a stock
        hold = Math.max(
            prevHold,
            prevCash - prices[i]
        );
    }

    return cash;
};
