
var filterRestaurants = function(restaurants, veganFriendly, maxPrice, maxDistance) {
    return restaurants
        .filter(([id, rating, vegan, price, distance]) => {
            return (veganFriendly === 0 || vegan === 1) &&
                   price <= maxPrice &&
                   distance <= maxDistance;
        })
        .sort((a, b) => {
            if (a[1] !== b[1]) {
                return b[1] - a[1];
            }

            return b[0] - a[0];
        })
        .map(restaurant => restaurant[0]);
};

