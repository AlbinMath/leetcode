var minTime = function(skill, mana) {
    const n = skill.length;
    const pref = new Array(n);
    pref[0] = skill[0];
    for (let i = 1; i < n; i++) {
        pref[i] = pref[i - 1] + skill[i];
    }

    // Completion times for potion 0 (starts at t = 0)
    const done = new Array(n);
    for (let i = 0; i < n; i++) {
        done[i] = pref[i] * mana[0];
    }

    for (let j = 1; j < mana.length; j++) {
        const currMana = mana[j];
        let startTime = done[0];

        for (let i = 1; i < n; i++) {
            const candidate = done[i] - pref[i - 1] * currMana;
            if (candidate > startTime) {
                startTime = candidate;
            }
        }

        for (let i = 0; i < n; i++) {
            done[i] = startTime + pref[i] * currMana;
        }
    }

    return done[n - 1];
};
