public class Solution {
    public ArrayList<ArrayList<Integer>> permute(int[] num) {
        ArrayList<ArrayList<Integer>> result = new ArrayList<ArrayList<Integer>>();
        if(num == null){
        	return result;
        }
        ArrayList<ArrayList<Integer>> r = new ArrayList<ArrayList<Integer>>();
        ArrayList<Integer> t= new ArrayList<Integer>();
        t.add(num[0]);
        result.add(t);
        for(int i = 1;i< num.length;i++){
        	r = result;
        	result = new ArrayList<ArrayList<Integer>>();
        	for(ArrayList<Integer> y:r){
        		for(int z=0;z <= y.size();z++){
        			ArrayList<Integer> tmp = new ArrayList<Integer>();
        			tmp.addAll(y);
        			tmp.add(z, num[i]);
        			result.add(tmp);
        		}
        	}
        }
        return result;
    }
}