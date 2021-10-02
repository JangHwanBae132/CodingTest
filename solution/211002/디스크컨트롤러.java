import java.util.*;
import java.util.stream.*;

class Solution {
    public int solution(int[][] jobs) {
        int answer = 0;
        Arrays.sort(jobs, Comparator.comparingInt(o1 -> o1[1]));
        Arrays.sort(jobs, Comparator.comparingInt(o1 -> o1[0]));
        PriorityQueue<int[]> h = new PriorityQueue<>(Comparator.comparingInt(o1 -> o1[1]));
        Queue<int[]> q = new LinkedList<>(Arrays.stream(jobs).collect(Collectors.toList()));

        int[] start = q.poll();
        int time = start[0];
        h.add(start);
        while (!h.isEmpty() || !q.isEmpty()){
            int[] poll = h.poll();
            time +=poll[1];
            answer += time-poll[0];
            if(q.isEmpty()) continue;

            while (!q.isEmpty()){
                if (q.peek()[0]<= time){
                    h.add(q.poll());
                } else break;
            }

            if (h.isEmpty() && q.peek()[0]> time){
                int[] poll1 = q.poll();
                time+=poll1[0]-time;
                h.add(poll1);
            }
        }
        return answer/jobs.length;
    }
}
