var canAliceWin = function(n) {
    let stonesNeeded = 10;
    let isAliceTurn = true;

    while (n >= stonesNeeded && stonesNeeded > 0) {
        n -= stonesNeeded;
        stonesNeeded--;
        isAliceTurn = !isAliceTurn;
    }

    return !isAliceTurn;
};
