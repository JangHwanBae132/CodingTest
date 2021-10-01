class Solution {
    public void sort(int[] data, int l, int r){
        int left = l;
        int right = r;
        int pivot = data[(l+r)/2];

        do{
            while(Long.parseLong(Integer.toString(data[left])+Integer.toString(pivot)) > Long.parseLong(Integer.toString(pivot)+Integer.toString(data[left])) ) left++;
            while(Long.parseLong(Integer.toString(data[right])+Integer.toString(pivot)) < Long.parseLong(Integer.toString(pivot)+Integer.toString(data[right])) ) right--;

            if(left <= right){
                int temp = data[left];
                data[left] = data[right];
                data[right] = temp;
                left++;
                right--;
            }
        }while (left <= right);

        if(l < right) sort(data, l, right);
        if(r > left) sort(data, left, r);
    }

    public String solution(int[] numbers){
        sort(numbers,0, numbers.length-1);
        String answer = "";
        if (numbers[0] == 0){
            return "0";
        }
        for (int number : numbers) {
            answer += Integer.toString(number);
        }
        return answer;
    }

}
