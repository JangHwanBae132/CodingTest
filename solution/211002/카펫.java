class Solution {
    public int[] solution(int brown, int yellow) {
        int[] answer = new int [2];
        
        int _b = brown/2+2;
        int _ac = 4*(brown+yellow);
        
              
        int x =  (int) (_b + Math.sqrt(_b*_b-_ac))/2;
        int y =  (int) (_b - Math.sqrt(_b*_b-_ac))/2;
        
        answer[0] =x;
        answer[1] =y;
        return answer;
    }
}
