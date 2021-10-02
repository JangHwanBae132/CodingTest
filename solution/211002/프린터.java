import java.util.*;
import java.util.stream.*;

class Solution {

    public int solution(int[] priorities, int location) {
        int answer = 0;
        Queue<Integer[]> queue = new LinkedList<>();
        HashMap<Integer, Integer> hashMap = new HashMap<>();

        for (int i =0;  i< priorities.length; i++ ){
            Integer[] Q_value = {i, priorities[i]};
            queue.add(Q_value);
            Integer value = hashMap.getOrDefault(priorities[i], 0);
            hashMap.put(priorities[i], value+1);
        }

        Queue<Integer> sortedKey = hashMap.keySet().stream().sorted(Comparator.reverseOrder()).collect(Collectors.toCollection(LinkedList::new));


        while (!queue.isEmpty()){
            Integer[] poll = queue.poll();
            if (poll[1] == sortedKey.peek()){
                if (poll[0] == location){
                    return answer+1;
                } else {
                    answer++;
                    hashMap.put(poll[1],hashMap.get(poll[1])-1);
                    if (hashMap.get(poll[1]) == 0){
                        sortedKey.poll();
                    }
                }
            } else {
                queue.add(poll);
            }
        }
        return answer;
    }

}
