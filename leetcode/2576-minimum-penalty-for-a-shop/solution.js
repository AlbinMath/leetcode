
var bestClosingTime = function(customers) {
    let penalty = 0;
    for (let char of customers) {
        if (char === 'Y') {
            penalty++;
        }
    }

    let minPenalty = penalty;
    let bestHour = 0;
    for (let i = 0; i < customers.length; i++) {
        if (customers[i] === 'Y') {
            penalty--;
        } else {
            penalty++;
        }
        if (penalty < minPenalty) {
            minPenalty = penalty;
            bestHour = i + 1;
        }
    }

    return bestHour;
};

