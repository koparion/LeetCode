class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        unordered_set<int> seen;  // Create an unordered_set to store unique elements seen so far
        for (int i = 0; i < nums.size(); ++i) {
            int num = nums[i]; // Iterate through each element 'num' in the input vector 'nums'     
            if (seen.find(num) != seen.end()) {
                return true;           // If 'num' is found in the set, it means there's a duplicate, return true
            }
                seen.insert(num);          // Otherwise, insert 'num' into the set
        }
    return false;                  // If loop completes without finding any duplicates, return false

    /* another way with for loop */
    // unordered_set<int> seen;  
    // for (int num : nums) {         
    //     if (seen.find(num) != seen.end()) {
    //         return true;           
    //     }
    //     seen.insert(num);         
    // }
    // return false;       
    }
};