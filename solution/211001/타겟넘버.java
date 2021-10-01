class Solution {
    public int solution(int[] numbers, int target) {
        int answer = dfs(numbers, 0, 0, target);
        return answer;
    }
    
    public int dfs(int[] numbers, int current, int depth, int target){
        if (depth == numbers.length){
            if (current == target){
                return 1;
            } else {
                return 0;
            }
        }
        
        return dfs(numbers, current + numbers[depth], depth+1 , target) + dfs(numbers, current - numbers[depth], depth+1 , target);
    }
    
}
