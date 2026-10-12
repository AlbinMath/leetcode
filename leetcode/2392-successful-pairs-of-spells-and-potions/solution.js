var successfulPairs = function(spells, potions, success) {
    potions.sort((a, b) => a - b);

    const m = potions.length;
    const pairs = [];

    for (const spell of spells) {
        let left = 0;
        let right = m - 1;

        while (left <= right) {
            const mid = Math.floor((left + right) / 2);

            if (spell * potions[mid] >= success) {
                right = mid - 1;
            } else {
                left = mid + 1;
            }
        }

        pairs.push(m - left);
    }

    return pairs;
};
