
var maxWeight = function(pizzas) {
    pizzas.sort((a, b) => a - b);

    const days = pizzas.length / 4;
    const oddDays = Math.ceil(days / 2);
    const evenDays = Math.floor(days / 2);

    let total = 0;
    let right = pizzas.length - 1;

    for (let i = 0; i < oddDays; i++) {
        total += pizzas[right];
        right--;
    }

    for (let i = 0; i < evenDays; i++) {
        total += pizzas[right - 1];
        right -= 2;
    }

    return total;
};

