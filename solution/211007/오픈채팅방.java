import java.util.*;

class Solution {
    public String[] solution(String[] record) {
        HashMap<String, String> hashMap = new HashMap<>();
        List<String[]> list = new ArrayList<>();
        for (String s : record) {
            String[] split_s = s.split(" ");
            if (split_s[0].equals("Enter")){
                hashMap.put(split_s[1], split_s[2]);
                String[] ans = {"0",split_s[1]};
                list.add(ans);
            } else if(split_s[0].equals("Change")){
                hashMap.put(split_s[1], split_s[2]);
            } else if(split_s[0].equals("Leave")){
                String[] ans = {"2",split_s[1]};
                list.add(ans);
            }
        }

        List<String> answer = new ArrayList<>();

        for (String[] s : list) {
            if (s[0].equals("0")){
                answer.add(hashMap.get(s[1])+"님이 들어왔습니다.");
            } else if (s[0].equals("2")){
                answer.add(hashMap.get(s[1])+"님이 나갔습니다.");
            }
        }

        return answer.toArray(new String[0]);
    }
}
