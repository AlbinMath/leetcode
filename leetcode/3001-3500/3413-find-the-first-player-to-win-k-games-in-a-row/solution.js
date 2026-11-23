var findWinningPlayer = function(skills, k) {
    let champion = 0;
    let streak = 0;

    for (let i = 1; i < skills.length; i++) {
        if (skills[i] > skills[champion]) {
            champion = i;
            streak = 1;
        } else {
            streak++;
        }

        if (streak === k) {
            return champion;
        }
    }

    return champion;
};
