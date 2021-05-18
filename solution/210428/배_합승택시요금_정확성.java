import java.util.*;

class Solution {
		static int map[][];
    static public int[][] makeMaps(int n, int[][] fares) {
    	int maps[][] = new int [n+1][n+1];
    	
    	for(int[] fare: fares) {
    		for(int i=1; i<n+1; i++) {
        		for(int j=i; j<n+1; j++) {
        			if((i==fare[0] && j==fare[1]) || (i==fare[1] && j==fare[0]) ) {
        				maps[i][j] = fare[2];
        				maps[j][i] = fare[2];
        			}
        		}

        	}
    	}
    	
    	
    	return maps;
    } 
    
    public static int dijkstra(int n, int s, int d ){

    	if(s==d) {
    		return 0;
    	}
    
        int newFare[] = new int[n+1];          //최단 거리를 저장할 변수
        boolean[] check = new boolean[n+1];     //해당 노드를 방문했는지 체크할 변수
        
        
	    //newFare값 초기화.
	    for(int i=1;i<n+1;i++){
	    	newFare[i] = 10000001;
	    }

         
        //시작노드값 초기화.
	    newFare[s] =0;
        check[s] =true;
         
        //연결노드 newFare갱신
        for(int i=1;i<n+1;i++){
            if(!check[i] && map[s][i]!=0){
            	newFare[i] = map[s][i];
            }

        }
         
         
        for(int a=0;a<n-1;a++){
            //원래는 모든 노드가 true될때까지 인데
            //노드가 n개 있을 때 다익스트라를 위해서 반복수는 n-1번이면 된다.
            //원하지 않으면 각각의 노드가 모두 true인지 확인하는 식으로 구현해도 된다.
            int min=10000001;
            int min_index=-1;
             
            //최소값 찾기
            for(int i=1;i<n+1;i++){
                if(!check[i] && newFare[i]!=10000001){
                    if(newFare[i]<min ){
                        min=newFare[i];
                        min_index = i;
                    }
                }
            }
            
            if(min_index == d) { 
            	return newFare[min_index];
            }
            
            if(min_index == -1) {
                return 10000001;
            }

            check[min_index] = true;
            
            
            for(int i=1;i<n+1;i++){
                if(!check[i] && map[min_index][i]!=0){
                    if(newFare[i]>newFare[min_index]+map[min_index][i]){
                        newFare[i] = newFare[min_index]+map[min_index][i];
                    }
                }
            }
        }
        return 10000001;
    }
 
    public static int solution(int n, int s, int a, int b, int[][] fares) {
    	map = makeMaps(n, fares);
        List<Integer> ansList = new ArrayList<Integer>();
         
        for(int i=1; i<n+1; i++) {
        	
           	ansList.add(dijkstra(n,s,i)+dijkstra(n,i,a )+dijkstra(n,i,b ));
        		
        	
        }
        

        return Collections.min(ansList);
    }
    
    public static void main(String[] args){
    	int n =7;
    	int s =3;
    	int a =4;
    	int b =1;
    	int[][] fares= {{5, 7, 9}, {4, 6, 4}, {3, 6, 1}, {3, 2, 3}, {2, 1, 6}}; 
    	
    	System.out.println("답: "+solution(n,s,a,b,fares));
    }
}    
