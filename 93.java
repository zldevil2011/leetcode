package JCode;

import java.util.ArrayList;
import java.util.List;

public class L93 {
	public List<String> restoreIpAddresses(String s) {
		List<String> res = new ArrayList<String>();
		if(s.length() < 4 || s.length() > 12){
			return res;
		}
		dfs(s, "", res, 1);
		return res;
    }
	public void dfs(String s, String temp, List<String> res, int cnt){
		if(cnt  == 4 && isValid(s)){
			res.add(temp + s);
			return;
		}
		for(int i = 1; i < Math.min(4, s.length()); ++i){
			String cur = s.substring(0, i);
			if(isValid(cur)){
				dfs(s.substring(i),  temp + cur + ".", res, cnt+1);
			}
		}
	}
	public boolean isValid(String s){
		if(s.charAt(0) == '0') return s.equals("0");
		int num = Integer.parseInt(s);
        return 0 < num && num < 256;
	}
	public static void main(String[] args){
		L93 l = new L93();
		List<String> ans = l.restoreIpAddresses("25525511135");
		int len = ans.size();
		for(int i = 0; i < len; ++i){
			System.out.println(ans.get(i));
		}
	}
}
