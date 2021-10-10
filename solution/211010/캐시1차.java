import java.util.*;

class Solution {
    public int solution(int cacheSize, String[] cities) {
        int answer = 0;
        Map<String ,Integer> map = new HashMap<>();

        if(cacheSize ==0){
            return 5*cities.length;
        }

        int cnt =0;
        for (String c : cities) {
            String city = c.toUpperCase(Locale.ROOT);
            cnt++;

            if (map.containsKey(city)){
                answer+=1;
                map.put(city,cnt);
            } else if(map.size()<cacheSize){
                answer+=5;
                map.put(city, cnt);
                continue;
            }

            if (!map.containsKey(city) && map.size() == cacheSize){
                answer+=5;
                List<String> keySetList = new ArrayList<>(map.keySet());
//                        Collections.sort(keySetList, ((o1, o2) -> (map.get(o1).compareTo(map.get(o2)))));
                Collections.sort(keySetList, (Comparator.comparing(map::get)));
                map.remove(keySetList.get(0));
                map.put(city,cnt);
            }
        }

        return answer;
    }
}
