from collections import deque
from typing import List

class RideSharingSystem:
    def __init__(self):
        self.riders = deque()
        self.drivers = deque()
        self.waiting = set()      # riders currently in the queue and not cancelled

    def addRider(self, riderId: int) -> None:
        self.riders.append(riderId)
        self.waiting.add(riderId)

    def addDriver(self, driverId: int) -> None:
        self.drivers.append(driverId)

    def matchDriverWithRider(self) -> List[int]:
        # discard cancelled riders at the front
        while self.riders and self.riders[0] not in self.waiting:
            self.riders.popleft()
        if not self.riders or not self.drivers:
            return [-1, -1]
        rider = self.riders.popleft()
        driver = self.drivers.popleft()
        self.waiting.discard(rider)
        return [driver, rider]

    def cancelRider(self, riderId: int) -> None:
        self.waiting.discard(riderId)   # no effect if matched, cancelled, or unknown
