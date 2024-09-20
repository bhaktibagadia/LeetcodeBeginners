class Solution {
    public List<List<Integer>> combinationSum(int[] candidates, int target) {
        List<List<Integer>> ans = new ArrayList<>();
        backtrack(candidates, target, 0, new ArrayList<>(), 0, ans);
        return ans;
    }
    private void backtrack(int[] candidates, int target, int i, List<Integer> ds, int summ, List<List<Integer>> ans){
        if (i==candidates.length){
            return;
        }
        if (summ==target){
            ans.add(new ArrayList<>(ds));
            return;
        }
        if (summ+candidates[i]<=target){
            ds.add(candidates[i]);
            summ+=candidates[i];
            backtrack(candidates, target, i, ds, summ, ans);
            summ-=candidates[i];
            ds.remove(ds.size()-1);
        }
        backtrack(candidates, target, i+1, ds, summ, ans);
    }
}