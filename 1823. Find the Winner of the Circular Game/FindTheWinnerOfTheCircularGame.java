class Solution {
    public int findTheWinner(int n, int k) {
        return findTheStart(n, k) + 1;
    }

    int findTheStart(int n, int k) {
        if (n == 1) {
            return 0;
        }
        return (findTheStart(n-1, k) + k) % n;
    }
}
