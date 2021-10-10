import java.util.*;

class Solution {
    int[][] vertical = {};
    int[][] horizontal = {};
    public int[][] solution(int n, int[][] build_frame) {
        int[][] answer = {};
        List<int[]> answerList = new ArrayList<>();
        vertical = new int[n+1][n+1];
        horizontal = new int[n+1][n+1];

        for (int[] frame : build_frame) {
            int x = frame[0];
            int y = frame[1];

            //기둥설치
            if (frame[2]==0 && frame[3]==1){
                if(canVertical(x,y)) vertical[x][y]=1;
            }

            //보 설치
            if (frame[2]==1 && frame[3]==1){
                if(canHorizontal(x,y)) horizontal[x][y]=1;
            }

            //기둥제거
            if (frame[2]==0 && frame[3]==0){
                vertical[x][y] =0;
                if(!canDeleteVertical(x,y)) vertical[x][y]=1;
            }

            //보 제거
            if (frame[2]==1 && frame[3]==0){
                horizontal[x][y] =0;
                if(!canDeleteHorizontal(x,y)) horizontal[x][y]=1;
            }
        }

        for(int i =0; i<n+1; i++){
            for(int j=0; j<n+1; j++){
                if(vertical[i][j]==1) answerList.add(new int[]{i,j,0});
            }
        }

        for(int i =0; i<n+1; i++){
            for(int j=0; j<n+1; j++){
                if(horizontal[i][j]==1) answerList.add(new int[]{i,j,1});
            }
        }
        int index =0;
        answerList.sort(Comparator.comparingInt(o->o[2]));
        answerList.sort(Comparator.comparingInt(o->o[1]));
        answerList.sort(Comparator.comparingInt(o->o[0]));
        return answerList.stream().toArray(int[][]::new);

    }

    public boolean canVertical(int x, int y){
        if(y==0) return true;
        if(vertical[x][y-1]==1) return true;
        if(horizontal[x][y]==1) return true;
        if(x>0 && horizontal[x-1][y]==1) return true;
        return false;
    }

    public boolean canHorizontal(int x, int y){
        if(vertical[x][y-1]==1) return true;
        if(vertical[x+1][y-1]==1) return true;
        if(x>0 && horizontal[x-1][y]==1 && horizontal[x+1][y]==1) return true;
        return false;
    }

    public boolean canDeleteVertical(int x, int y){
        if(vertical[x][y+1]==1 && !canVertical(x,y+1))return false;

        if(horizontal[x][y+1]==1 && !canHorizontal(x,y+1))return false;

        if(x>0 && horizontal[x-1][y+1]==1 && !canHorizontal(x-1,y+1))return false;

        return true;
    }

    public boolean canDeleteHorizontal(int x, int y){
        if(vertical[x][y]==1 && !canVertical(x,y)) return false;

        if(vertical[x+1][y]==1 && !canVertical(x+1,y)) return false;

        if(x>0 && horizontal[x-1][y]==1 && !canHorizontal(x-1,y))return false;

        if(horizontal[x+1][y]==1&&!canHorizontal(x+1,y))return false;

        return true;
    }
}
