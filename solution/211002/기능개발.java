import java.util.*;
import java.util.stream.Collectors;

class Solution {
    public int[] solution(int[] progresses, int[] speeds) {
        Queue<Integer> queue = new LinkedList<>();
        queue.addAll(Arrays.stream(progresses).boxed().collect(Collectors.toList()));
        
        List<Integer> answer = new ArrayList<>();

        int day = 0;
        int index = 0;
        while (!queue.isEmpty()){
            day+=1;
            int cnt = 0;
            while (!queue.isEmpty()){
                Integer peek = queue.peek();
                if (peek+day*speeds[index]>=100){
                    queue.poll();
                    cnt+=1;
                    index +=1;
                } else {
                    break;
                }
            }
            if (cnt !=0){
                answer.add(cnt);
            }
        }
        return  answer.stream().mapToInt(i -> i).toArray();
    }

}
