var lastStoneWeight = function(stones) {
    while (stones.length > 1) {
        stones.sort((a, b) => b - a);

        let y = stones.shift(); // Heaviest stone
        let x = stones.shift(); // Second heaviest stone

        if (y !== x) {
            stones.push(y - x);
        }
    }

    return stones.length === 0 ? 0 : stones[0];
};
