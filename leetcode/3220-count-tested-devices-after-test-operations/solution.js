var countTestedDevices = function(batteryPercentages) {
    let tested = 0;
    for (const battery of batteryPercentages) {
        if (battery > tested) {
            tested++;
        }
    }
    return tested;
};
