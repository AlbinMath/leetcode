class Solution {
    function minDepth($root) {
        if ($root === null) {
            return 0;
        }

        $queue = [$root];
        $front = 0;
        $depth = 1;

        while ($front < count($queue)) {
            $levelSize = count($queue) - $front;

            for ($i = 0; $i < $levelSize; $i++) {
                $node = $queue[$front++];

                // First leaf found = minimum depth
                if ($node->left === null && $node->right === null) {
                    return $depth;
                }

                if ($node->left !== null) {
                    $queue[] = $node->left;
                }

                if ($node->right !== null) {
                    $queue[] = $node->right;
                }
            }

            $depth++;
        }

        return $depth;
    }
}
