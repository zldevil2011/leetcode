public class L97 {
	public boolean isInterleave(String s1, String s2, String s3) {
        int m = s1.length(), n = s2.length();
        if(m + n != s3.length()){
        	return false;
        }
        boolean nums[][] = new boolean[m+1][n+1];
        for(int i = 0; i < m; ++i){
        	for(int j = 0; j < n; ++j){
        		nums[i][j] = false;
        	}
        }
        for(int i = 0; i < m + 1; ++i){
        	for(int j = 0; j < n + 1; ++j){
        		if(i == 0 && j == 0){
        			nums[i][j] = true;
        		}else if(i == 0){
        			nums[i][j] = nums[i][j-1] & (s2.charAt(j-1) == s3.charAt(j-1));
        		}else if(j == 0){
        			nums[i][j] = nums[i-1][j] & (s1.charAt(i-1) == s3.charAt(i-1));
        		}else{
        			nums[i][j] = (nums[i][j-1] & (s2.charAt(j-1) == s3.charAt(i+j-1))) || (
        					nums[i-1][j] & (s1.charAt(i-1) == s3.charAt(i+j-1)));
        		}
        	}
        }
        
		return nums[m][n];
    }
	public static void main(String[] args){
		String s1 = "aabcc";
		String s2 = "dbbca";
//		String s3 = "aadbbcbcac";
		String s3 = "aadbbbaccc";
		L97 l = new L97();
		System.out.println(l.isInterleave(s1, s2, s3));
	}
}
