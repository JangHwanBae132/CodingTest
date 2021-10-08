import java.util.*;
import java.util.stream.Collectors;

class Solution {
    public int solution(String[] lines) {
        int answer = 0;
        List<Integer[]> list = new ArrayList<>();
        List<Integer> checkPoint = new ArrayList<>();
        for (String line : lines) {
            Integer[] el = new Integer[2];
            String[] sp = line.split(" ");
            String[] sp2 = sp[1].split(":");
            String[] sp3 = sp2[2].split("\\.");
            el[1] = (Integer.parseInt(sp2[0])*60*60+Integer.parseInt(sp2[1])*60)*1000+
                    Integer.parseInt(sp3[0])*1000+Integer.parseInt(sp3[1]);
            el[0] = el[1] - (int)(Float.parseFloat(sp[2].replaceFirst(".$", ""))*1000)+1;
            list.add(el);
        }

        list.sort(Comparator.comparingInt(o1 -> o1[0]));
        Integer minValue = list.get(0)[0];

        Queue<Integer[]> queue = list.stream().map((o1) -> {
            o1[0] = o1[0] - minValue;
            o1[1] = o1[1] - minValue;
            checkPoint.add(o1[0]);
            checkPoint.add(o1[1]);
            return o1;
        }).collect(Collectors.toCollection(LinkedList::new));

        checkPoint.sort(Comparator.comparingInt(o->o));

        PriorityQueue<Integer> heap = new PriorityQueue<>();

        for (Integer point : checkPoint) {
            while (!queue.isEmpty()){
                Integer[] peek = queue.peek();
                if(peek[0]<= point+999){
                    heap.add(queue.poll()[1]);
                } else {
                    break;
                }
            }

            while (!heap.isEmpty()){
                Integer peek = heap.peek();
                if(peek < point){
                    heap.poll();
                } else {
                    break;
                }
            }

            answer = (answer<heap.size())? heap.size():answer;
        }


        return answer;
    }
}
