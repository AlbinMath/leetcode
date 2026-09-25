class DiningPhilosophers {
private:
    mutex forks[5];

public:
    DiningPhilosophers() {
        
    }

    void wantsToEat(int philosopher,
                    function<void()> pickLeftFork,
                    function<void()> pickRightFork,
                    function<void()> eat,
                    function<void()> putLeftFork,
                    function<void()> putRightFork) {

        int left = philosopher;
        int right = (philosopher + 1) % 5;

        unique_lock<mutex> leftLock(forks[left], defer_lock);
        unique_lock<mutex> rightLock(forks[right], defer_lock);

        // Acquire both forks without deadlock
        lock(leftLock, rightLock);

        // Pick forks
        pickLeftFork();
        pickRightFork();

        // Eat
        eat();

        // Put forks down
        putLeftFork();
        putRightFork();

        // unique_lock automatically unlocks here
    }
};
