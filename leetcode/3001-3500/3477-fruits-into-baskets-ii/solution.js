var numOfUnplacedFruits = function(fruits, baskets) {
    let unplaced = 0;

    for (const fruit of fruits) {
        let placed = false;
        for (let j = 0; j < baskets.length; j++) {
            if (baskets[j] >= fruit) {
                baskets[j] = 0; // Mark basket as occupied
                placed = true;
                break;
            }
        }
        if (!placed) {
            unplaced++;
        }
    }

    return unplaced;
};
