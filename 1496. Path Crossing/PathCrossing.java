class Solution {
    public boolean isPathCrossing(String path) {
        Set<Integer> coords = new HashSet<>();
        int x = 0, y = 0;
        coords.add(0);

        for (char dir : path.toCharArray()) {
            switch (dir) {
                case 'N': y++; break;
                case 'S': y--; break;
                case 'E': x++; break;
                case 'W': x--; break;
            }
            int encodedCoord = encode(x, y);
            if (coords.contains(encodedCoord)) {
                return true;
            }
            coords.add(encodedCoord);
        }

        return false;
    }

    int encode(int x, int y) {
        return (x << 16) | (y & 0xffff);
    }
}
