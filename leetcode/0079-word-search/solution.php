class Solution {
    function exist($board, $word) {
        $rows = count($board);
        $cols = count($board[0]);

        for ($r = 0; $r < $rows; $r++) {
            for ($c = 0; $c < $cols; $c++) {

                if ($this->dfs($board, $word, $r, $c, 0, $rows, $cols)) {
                    return true;
                }
            }
        }

        return false;
    }

    function dfs(&$board, $word, $row, $col, $index, $rows, $cols) {

        // All characters matched
        if ($index == strlen($word)) {
            return true;
        }

        // Out of bounds
        if ($row < 0 || $row >= $rows ||
            $col < 0 || $col >= $cols) {
            return false;
        }

        // Current character doesn't match
        if ($board[$row][$col] != $word[$index]) {
            return false;
        }

        // Mark as visited
        $temp = $board[$row][$col];
        $board[$row][$col] = '#';

        // Search four directions
        $found =
            $this->dfs($board, $word, $row + 1, $col, $index + 1, $rows, $cols) ||
            $this->dfs($board, $word, $row - 1, $col, $index + 1, $rows, $cols) ||
            $this->dfs($board, $word, $row, $col + 1, $index + 1, $rows, $cols) ||
            $this->dfs($board, $word, $row, $col - 1, $index + 1, $rows, $cols);

        // Restore cell
        $board[$row][$col] = $temp;

        return $found;
    }
}
