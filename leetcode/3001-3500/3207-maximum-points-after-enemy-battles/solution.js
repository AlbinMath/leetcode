
var maximumPoints = function(enemyEnergies, currentEnergy) {
    const minEnergy = Math.min(...enemyEnergies);

    if (currentEnergy < minEnergy) {
        return 0;
    }

    let totalEnergy = currentEnergy;

    let skippedMin = false;

    for (const energy of enemyEnergies) {
        if (energy === minEnergy && !skippedMin) {
            skippedMin = true;
            continue;
        }

        totalEnergy += energy;
    }

    return Math.floor(totalEnergy / minEnergy);
};

