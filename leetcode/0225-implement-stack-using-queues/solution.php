class MyStack {

    private $queue1;
    private $queue2;

    function __construct() {
        $this->queue1 = [];
        $this->queue2 = [];
    }

    function push($x) {
        // Add new element to the temporary queue
        $this->queue2[] = $x;

        // Move all existing elements behind it
        while (!empty($this->queue1)) {
            $this->queue2[] = array_shift($this->queue1);
        }

        // Swap the queues
        $temp = $this->queue1;
        $this->queue1 = $this->queue2;
        $this->queue2 = $temp;
    }

    function pop() {
        return array_shift($this->queue1);
    }

    function top() {
        return $this->queue1[0];
    }

    function empty() {
        return empty($this->queue1);
    }
}
