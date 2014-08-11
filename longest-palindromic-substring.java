public class Solution {
    public String longestPalindrome(String s) {
    	if( s == null || s.length()==0){
    		return "";
    	}
    	StringBuffer sb = new StringBuffer();

        for(char c:s.toCharArray()){
        	sb.append('#');
        	sb.append(c);        	
        }
        sb.append('#');
        String newstr = sb.toString();
        String result = "";
        int len = 0;
        for(int i = 0;i <newstr.length();i++){
        	int index = 1;
        	int count = 0;
        	while(i-index>=0&&i+index<newstr.length()&&newstr.charAt(i-index)==newstr.charAt(i+index)){
        		index ++;
        		count ++;
        	}
        	if(count>len){
        		len = count;
        		result = newstr.substring(i-index+1, i+index);
        	}
        }
        sb = new StringBuffer();
        for(char c:result.toCharArray()){
        	if(c !='#'){
        		sb.append(c);
        	}
        }
        return sb.toString();
    }
}