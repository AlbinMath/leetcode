var distanceTraveled = function(mainTank, additionalTank) {
    const transfers = Math.min(additionalTank, Math.floor((mainTank - 1) / 4));
    return (mainTank + transfers) * 10;
};
