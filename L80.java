package JCode;

import java.util.HashMap;
import java.util.Map;

public class L80 {
	public int removeDuplicates(int[] nums) {
		Map<Integer, Integer> test = new HashMap<Integer, Integer>();
		int len = nums.length;
		for(int i = 0; i < len; ++i){
			try{
				Integer pre = test.get(nums[i]);
				test.put(nums[i], pre + 1);
			}catch(Exception e){
				test.put(nums[i], 1);
			}
		}
		int ans = 0;
		for(Integer key : test.keySet()){
			Integer value = test.get(key);  
			if(value >= 2){
				ans += 2;
			}else{
				ans += value;
			}
//		    System.out.println("Key = " + key + ", Value = " + value);  
		}
		return ans;
	}
	public static void main(String[] args){
		int[] input = {1,1,1,2};
		L80 l80 = new L80();
		int ans = l80.removeDuplicates(input);
		System.out.println(ans);
	}
}
