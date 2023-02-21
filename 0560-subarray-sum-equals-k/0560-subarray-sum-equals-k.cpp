class Solution {
public:
    int subarraySum(vector<int>& nums, int k) {
        unordered_map<int,int> mp;
        int prefixsum=0,ans=0;
        mp[0] = 1;
        for(auto it:nums){
            prefixsum += it;
            int difference = prefixsum - k;
            if(mp.find(difference) != mp.end()){
                ans += mp[difference];
            }
            mp[prefixsum]++;
        }
        return ans;
    }
};