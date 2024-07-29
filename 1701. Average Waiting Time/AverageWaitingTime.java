class Solution {
    public double averageWaitingTime(int[][] customers) {
        int time = 0;
        long totalWaitingTime = 0;
        for (int[] customer : customers) {
            time = Math.max(time, customer[0]) + customer[1];
            totalWaitingTime += time - customer[0];
        }
        return (double) totalWaitingTime / customers.length;
    }
}
