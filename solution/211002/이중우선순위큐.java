import java.util.*;

class Solution {
    public int[] solution(String[] operations) {
        int[] answer = new int[2];
        List<String> del = new ArrayList<>();
        PriorityQueue<Integer> min_q = new PriorityQueue<>();
        PriorityQueue<Integer> max_q = new PriorityQueue<>(Comparator.reverseOrder());
        int que = 0;
        for (String o : operations){
            if (que == 0){
                System.out.println("o = " + o);
                min_q.clear();
                max_q.clear();
            }

            if(o.equals("D 1")){
                if (que>0){
                    max_q.poll();
                    que--;
                }
            } else if(o.equals("D -1")){
                if (que>0){
                    min_q.poll();
                    que--;
                }
            } else{
                String[] s = o.split(" ");

                min_q.add(Integer.parseInt(s[1]));
                max_q.add(Integer.parseInt(s[1]));
                que++;
            }
        }

        if (que ==0){
            answer = new int[]{0, 0};
            return answer;
        } else {
            answer = new int[]{max_q.poll(), min_q.poll()}; 
            return answer;
        }

    }
}
