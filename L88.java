package JCode;

public class L88 {
	public void merge(int[] nums1, int m, int[] nums2, int n) {
        int[] temp = new int[1000000];
        int i = 0, j = 0, total = 0;
        while(i < m && j < n){
        	int t1 = nums1[i];
        	int t2 = nums2[j];
        	if(t1 < t2){
        		temp[total++] = t1;
        		i ++;
        	}else{
        		temp[total++] = t2;
        		j ++;
        	}
        }
        while(i < m){
        	int t1 = nums1[i];
        	temp[total++] = t1;
        	i ++;
        }
        while(j < n){
        	int t2 = nums2[j];
        	temp[total++] = t2;
        	j ++;
        }
        
        for(i = 0; i < total; ++i){
        	nums1[i] = temp[i];
        	System.out.println(nums1[i]);
        }
    }
	public static void main(String[] args){
		L88 l = new L88();
		int[] nums1 = {1,2,3,0,0,0};
		int m = 3;
		int[] nums2 = {2,5,6};
		int n = 3;
		l.merge(nums1, m, nums2, n);
	}
}
