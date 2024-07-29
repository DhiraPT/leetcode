class Solution {
    public int numTeams(int[] rating) {
        int n = rating.length;
        int teams = 0;
        TreeSet<Integer> left = new TreeSet<>();
        TreeSet<Integer> right = new TreeSet<>();

        for (int r : rating) {
            right.add(r);
        }

        for (int r : rating) {
            right.remove(r);
            int lessLeft = left.headSet(r).size();
            int moreLeft = left.size() - lessLeft;
            int lessRight = right.headSet(r).size();
            int moreRight = right.size() - lessRight;
            teams += lessLeft * moreRight + moreLeft * lessRight;
            left.add(r);
        }

        return teams;
    }
}
