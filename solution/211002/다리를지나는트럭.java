import java.util.*;
import java.util.stream.Collectors;

class Solution {

    public int solution(int bridge_length, int weight, int[] truck_weights) {
        int answer =1;
        Queue<Integer> truckQueue = new LinkedList<>(Arrays.stream(truck_weights).boxed().collect(Collectors.toList()));
        Queue<Integer[]> bridgeQueue = new LinkedList<>();

        int total = truck_weights[0];
        Integer[] start = {truckQueue.poll(),1};
        bridgeQueue.add(start);

        while (!bridgeQueue.isEmpty()){
            answer+=1;
            if(answer-bridgeQueue.peek()[1] >= bridge_length){
                total += -bridgeQueue.poll()[0];
            }

            if(truckQueue.isEmpty()) continue;

            if(bridgeQueue.size() < bridge_length && truckQueue.peek()+total<=weight){
                Integer[] truck = {truckQueue.poll(),answer};
                total += truck[0];
                bridgeQueue.add(truck);
            }

        }

        return answer;
    }

}
