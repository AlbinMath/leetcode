
var numTeams = function(rating) {
    const n = rating.length;
    let teams = 0;

    for (let j = 1; j < n - 1; j++) {
        let leftSmaller = 0;
        let leftGreater = 0;
        let rightSmaller = 0;
        let rightGreater = 0;

        // Count ratings to the left of j
        for (let i = 0; i < j; i++) {
            if (rating[i] < rating[j]) {
                leftSmaller++;
            } else {
                leftGreater++;
            }
        }

        // Count ratings to the right of j
        for (let k = j + 1; k < n; k++) {
            if (rating[k] < rating[j]) {
                rightSmaller++;
            } else {
                rightGreater++;
            }
        }

        // Increasing and decreasing teams
        teams += leftSmaller * rightGreater;
        teams += leftGreater * rightSmaller;
    }

    return teams;
};

