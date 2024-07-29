class Solution {
    public List<Integer> survivedRobotsHealths(int[] positions, int[] healths, String directions) {
        Robot[] robots = new Robot[positions.length];
        for (int i = 0; i < positions.length; i++) {
            robots[i] = new Robot(i, positions[i], healths[i], directions.charAt(i));
        }

        Arrays.sort(robots, (r1, r2) -> Integer.compare(r1.position, r2.position));
        Deque<Robot> stack = new ArrayDeque<>();

        for (Robot r : robots) {
            if (r.direction == 'R') {
                stack.push(r);
            } else {
                while (!stack.isEmpty() && stack.peek().direction == 'R') {
                    Robot leftRobot = stack.peek();
                    if (leftRobot.health > r.health) {
                        leftRobot.health -= 1;
                        r.health = 0;
                        break;
                    } else if (leftRobot.health < r.health) {
                        r.health -= 1;
                        stack.pop();
                    } else {
                        stack.pop();
                        r.health = 0;
                        break;
                    }
                }
                if (r.health > 0) {
                    stack.push(r);
                }
            }
        }

        List<Robot> sRobots = new ArrayList<>();
        while (!stack.isEmpty()) {
            sRobots.add(stack.pop());
        }

        Collections.sort(sRobots, (r1, r2) -> Integer.compare(r1.order, r2.order));

        List<Integer> sHealth = new ArrayList<>();
        for (Robot r : sRobots) {
            sHealth.add(r.health);
        }

        return sHealth;
    }
}

class Robot {
    int order;
    int position;
    int health;
    char direction;
    
    public Robot(int order, int position, int health, char direction) {
        this.order = order;
        this.position = position;
        this.health = health;
        this.direction = direction;
    }
}
