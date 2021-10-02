import java.util.*;
import java.util.stream.*;

class Solution {
    public String solution(String number, int k) {
        String answer = "";
        String[] split = number.split("");
        if (number.length()==1){
            return "";
        }
 
        Queue<String> que = Arrays.stream(split).collect(Collectors.toCollection(LinkedList::new));
        Stack<String> stack = new Stack<>();

        int del =0;
        while (del!=k){
            if(que.isEmpty()){
                stack.pop();
                del++;
                continue;
            }
            if(stack.isEmpty()){
                stack.add(que.poll());
                continue;
            }

            if (Integer.parseInt(stack.peek()) < Integer.parseInt(que.peek())){
                stack.pop();
                del++;
            } else {
                stack.add(que.poll());
            }
        }

        for (String s : stack) {
            answer +=s;
        }
        for (String s : que) {
            answer +=s;
        }

        return answer;
    }
}
