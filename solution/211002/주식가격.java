import java.util.*;
import java.util.stream.Collectors;

class Solution {

    public int[] solution(int[] prices) {
        int[] answer = new int[prices.length];
        Stack<Integer> stack = new Stack<>();
        stack.addAll(Arrays.stream(prices).boxed().collect(Collectors.toList()));

        Deque<Integer> list = new ArrayDeque<>();

        for (int i = prices.length-1 ; i>=0; i--){
            int count =-1;
            Integer pop = stack.pop();
            list.addFirst(pop);
            for (Integer price : list) {
                count++;
                if (prices[i] > price) break;
            }
            answer[i] = count;
        }
       
        return answer;
    }

}
