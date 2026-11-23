
var minMutation = function(startGene, endGene, bank) {
    if (startGene === endGene) return 0;

    const validGenes = new Set(bank);
    if (!validGenes.has(endGene)) return -1;

    const genes = ["A", "C", "G", "T"];
    const queue = [[startGene, 0]];
    const visited = new Set([startGene]);

    let front = 0;

    while (front < queue.length) {
        const [gene, mutations] = queue[front++];

        // Try changing each character
        for (let i = 0; i < gene.length; i++) {
            for (const char of genes) {
                if (gene[i] === char) continue;

                const nextGene =
                    gene.slice(0, i) +
                    char +
                    gene.slice(i + 1);

                if (
                    validGenes.has(nextGene) &&
                    !visited.has(nextGene)
                ) {
                    if (nextGene === endGene) {
                        return mutations + 1;
                    }

                    visited.add(nextGene);
                    queue.push([nextGene, mutations + 1]);
                }
            }
        }
    }

    return -1;
};

