var minimumAddedCoins = function(coins, target) {
    coins.sort((a, b) => a - b);

    let missing = 1;
    let i = 0;
    let count = 0;

    while (missing <= target) {
        if (i < coins.length && coins[i] <= missing) {
            missing += coins[i];
            i++;
        } else {
            missing *= 2;
            count++;
        }
    }

    return count;
};
