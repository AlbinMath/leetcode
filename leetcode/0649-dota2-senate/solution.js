var predictPartyVictory = function(senate) {
    const radiant = [];
    const dire = [];
    const n = senate.length;

    // Store each senator's index in their party's queue
    for (let i = 0; i < n; i++) {
        if (senate[i] === 'R') {
            radiant.push(i);
        } else {
            dire.push(i);
        }
    }

    // Simulate voting rounds
    while (radiant.length > 0 && dire.length > 0) {
        const r = radiant.shift();
        const d = dire.shift();

        // The senator with the earlier index bans the other
        if (r < d) {
            radiant.push(r + n);
        } else {
            dire.push(d + n);
        }
    }

    return radiant.length > 0 ? "Radiant" : "Dire";
};
