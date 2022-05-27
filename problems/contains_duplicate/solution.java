class Solution {
    public boolean containsDuplicate(int[] nums) {
        Set<Integer> num = new HashSet<Integer>();
        for(int i : nums){
             if(num.contains(i)){
                 return true;
             }
                
            num.add(i);
        }
        return false;
    }
}