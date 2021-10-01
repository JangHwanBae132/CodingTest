import java.util.*;

class Solution {
    public int solution(int n, int[][] computers) {
        int[] visited = new int[n];
        int answer = 0;
        HashMap<Integer, List<Integer>> hashMap = new HashMap<>();
        Queue<Integer> queue = new LinkedList<>();
        for (int i =0; i<n; i++){
            for (int j =0; j<i; j++){ 
                if (computers[i][j]==1){
                    List<Integer> values_i = hashMap.getOrDefault(i, new ArrayList<>());
                    values_i.add(j);
                    hashMap.put(i, values_i);
                        
                    List<Integer> values_j = hashMap.getOrDefault(j, new ArrayList<>());
                    values_j.add(i);
                    hashMap.put(j, values_j);
                }
            }
        }
        
        for(int i =0; i<n; i++){
            if (visited[i]==0){
                ++answer;
                queue.add(i);
                visited[i] =1;
                while(!queue.isEmpty()){
                    Integer poll = queue.poll();
                    if(hashMap.containsKey(poll)){
                        for (Integer node: hashMap.get(poll)){
                            if(visited[node]==0){
                                queue.add(node);
                                visited[node] =1;
                            }
                        }
                    }
                }
            }
        }
        
        return answer;
    }
}
