class Solution {
    public double angleClock(int hour, int minutes) {
        // Minute hand: 6 degrees per minute
        double minuteAngle = minutes * 6.0;

        // Hour hand: 30 degrees per hour + 0.5 degrees per minute
        double hourAngle = (hour % 12) * 30.0 + minutes * 0.5;

        double angle = Math.abs(hourAngle - minuteAngle);

        // Return the smaller angle
        return Math.min(angle, 360.0 - angle);
    }
}
