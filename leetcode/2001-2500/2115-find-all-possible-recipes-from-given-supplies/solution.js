/**
 * @param {string[]} recipes
 * @param {string[][]} ingredients
 * @param {string[]} supplies
 * @return {string[]}
 */
var findAllRecipes = function (recipes, ingredients, supplies) {
    const n = recipes.length;
    const users = new Map(); // ingredient -> indices of recipes needing it
    const indeg = new Array(n);

    for (let i = 0; i < n; i++) {
        indeg[i] = ingredients[i].length;
        for (const ing of ingredients[i]) {
            if (!users.has(ing)) users.set(ing, []);
            users.get(ing).push(i);
        }
    }

    const queue = [...supplies];
    const res = [];
    let head = 0;
    while (head < queue.length) {
        const x = queue[head++];
        const list = users.get(x);
        if (!list) continue;
        for (const r of list) {
            if (--indeg[r] === 0) {
                res.push(recipes[r]);
                queue.push(recipes[r]);
            }
        }
    }
    return res;
};
