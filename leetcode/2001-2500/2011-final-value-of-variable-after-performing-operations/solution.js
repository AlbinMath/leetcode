
var finalValueAfterOperations = function(operations) {
    let X = 0;

    for (const operation of operations) {
        if (operation.includes("+")) {
            X++;
        } else {
            X--;
        }
    }

    return X;
};

