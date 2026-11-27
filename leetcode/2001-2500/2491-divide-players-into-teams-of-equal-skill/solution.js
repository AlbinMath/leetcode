
var dividePlayers = function(skill) {
    skill.sort((a, b) => a - b);

    const n = skill.length;

    const total = skill.reduce((sum, value) => sum + value, 0);
    const target = total / (n / 2);

    let left = 0;
    let right = n - 1;

    let chemistry = 0;

    while (left < right) {
        const teamSkill = skill[left] + skill[right];
        if (teamSkill !== target) {
            return -1;
        }

        chemistry += skill[left] * skill[right];

        left++;
        right--;
    }

    return chemistry;
};

