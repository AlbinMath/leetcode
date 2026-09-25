class H2O {
private:
    mutex mtx;
    condition_variable cv;
    int hydrogenCount = 0;
    int oxygenCount = 0;
public:
    H2O() {
        
    }
    void hydrogen(function<void()> releaseHydrogen) {
        unique_lock<mutex> lock(mtx);
        cv.wait(lock, [&]() {
            return hydrogenCount < 2;
        });
        hydrogenCount++;
        releaseHydrogen();
        if (hydrogenCount == 2) {
            cv.notify_all();
        }
    }
    void oxygen(function<void()> releaseOxygen) {
        unique_lock<mutex> lock(mtx);
        cv.wait(lock, [&]() {
            return hydrogenCount == 2 && oxygenCount == 0;
        });
        oxygenCount++;
        releaseOxygen();
        hydrogenCount = 0;
        oxygenCount = 0;
        cv.notify_all();
    }
};
