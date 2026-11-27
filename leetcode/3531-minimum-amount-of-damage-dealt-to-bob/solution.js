
var minDamage = function(power, damage, health) {
    const n = damage.length;
    const enemies = [];

    for (let i = 0; i < n; i++) {
        const time = Math.ceil(health[i] / power);

        enemies.push({
            time: time,
            damage: damage[i]
        });
    }
    enemies.sort((a, b) => {
        return a.time * b.damage - b.time * a.damage;
    });

    let totalDamage = 0;
    let elapsedTime = 0;

    for (const enemy of enemies) {
        elapsedTime += enemy.time;
        totalDamage += elapsedTime * enemy.damage;
    }

    return totalDamage;
};

