class Solution {
    public int solution(int[] scoville, int K) {
        int answer = 0;
        boolean isCan = false;
        PriorityQueue<Integer> p = new PriorityQueue<>();
        p.addAll(Arrays.stream(scoville).boxed().collect(Collectors.toList()));
        while (!p.isEmpty()){
            Integer poll = p.poll();
            if (poll >= K) {
                isCan = true;
                break;
            } else if (p.isEmpty()) {
                break;
            } else {
                p.add(poll+p.poll()*2);
                answer++;
            }
        }
        return (isCan) ? answer : -1;
    }
}
