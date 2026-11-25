
var maximumEnergy = function(energy, k) {
    const n = energy.length;

    let ans = -Infinity;

    for (let i = n - 1; i >= 0; i--) {

        if (i + k < n) {
            energy[i] += energy[i + k];
        }

        ans = Math.max(ans, energy[i]);
    }

    return ans;
};

