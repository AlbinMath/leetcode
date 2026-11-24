var maxBottlesDrunk = function(numBottles, numExchange) {
    let drunk = numBottles;
    let empty = numBottles;

    while (empty >= numExchange) {
        empty -= numExchange - 1;
        numExchange++;
        drunk++;
    }

    return drunk;
};
