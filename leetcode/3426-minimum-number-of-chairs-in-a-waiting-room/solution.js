var minimumChairs = function(s) {
    let currentPeople = 0;
    let maxChairs = 0;

    for (const event of s) {
        if (event === 'E') {
            currentPeople++;
            if (currentPeople > maxChairs) {
                maxChairs = currentPeople;
            }
        } else {
            currentPeople--;
        }
    }

    return maxChairs;
};
