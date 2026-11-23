function buildArray(target: number[], n: number): string[] {
    const result: string[] = [];
    let index = 0;

    for (let num = 1; num <= n && index < target.length; num++) {
        result.push("Push");

        if (num === target[index]) {
            index++;
        } else {
            result.push("Pop");
        }
    }

    return result;
}
