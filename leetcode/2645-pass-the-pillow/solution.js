var passThePillow = function(n, time) {
    const fullTrips = Math.floor(time / (n - 1));
    const remainder = time % (n - 1);

    if (fullTrips % 2 === 0) {
        return 1 + remainder;
    }
    return n - remainder;
};
