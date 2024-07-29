class Solution {
    public String countOfAtoms(String formula) {
        Map<String, Integer> atms = new HashMap<>();
        Deque<Integer> muls = new ArrayDeque<>();

        StringBuilder m = new StringBuilder();
        StringBuilder a = new StringBuilder();

        int i = formula.length() - 1;
        int mul = 1;
        muls.push(mul);

        while (i >= 0) {
            char c = formula.charAt(i);
            if (Character.isDigit(c)) {
                m.append(c);
            } else if (c == ')') {
                mul = 1;
                if (m.length() > 0) {
                    mul = Integer.parseInt(m.reverse().toString());
                    m.setLength(0);
                }
                muls.push(mul * muls.peek());
            } else if (c == '(') {
                muls.pop();
            } else if (Character.isLowerCase(c)) {
                a.append(c);
            } else if (Character.isUpperCase(c)) {
                a.append(c);
                a.reverse();
                String atm = a.toString();
                a.setLength(0);
                mul = 1;
                if (m.length() > 0) {
                    mul = Integer.parseInt(m.reverse().toString());
                    m.setLength(0);
                }
                atms.put(atm, atms.getOrDefault(atm, 0) + mul * muls.peek());
            }
            i--;
        }

        TreeMap<String, Integer> sortedAtms = new TreeMap<>(atms);
        StringBuilder res = new StringBuilder();
        for (Map.Entry<String, Integer> entry : sortedAtms.entrySet()) {
            res.append(entry.getKey());
            if (entry.getValue() > 1) {
                res.append(entry.getValue());
            }
        }

        return res.toString();
    }
}
