class MyQueue {

    private $inStack = [];
    private $outStack = [];

    function __construct() {
    }

    function push($x) {
        // Always push new elements into inStack
        $this->inStack[] = $x;
    }

    function pop() {
        $this->moveToOutStack();

        return array_pop($this->outStack);
    }

    function peek() {
        $this->moveToOutStack();

        return $this->outStack[count($this->outStack) - 1];
    }

    function empty() {
        return empty($this->inStack) && empty($this->outStack);
    }

    private function moveToOutStack() {
        // Only transfer when outStack is empty
        if (empty($this->outStack)) {
            while (!empty($this->inStack)) {
                $this->outStack[] = array_pop($this->inStack);
            }
        }
    }
}
