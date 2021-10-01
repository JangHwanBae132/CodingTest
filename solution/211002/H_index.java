import java.util.*;

class Solution {
    public int solution(int[] citations) {
        int answer = 0;
        Integer[] cit_list = Arrays.stream(citations).boxed().toArray(Integer[]::new);
        Arrays.sort(cit_list, Collections.reverseOrder());
        for (int i = 0; i< cit_list.length; i++){
            if (cit_list[i]>= i+1){
                ++answer;
            } else {
                break;
            }
        }

        return answer;
    }
}
