class Solution {
public:
    long long countPairs(vector<int>& nums, int k) {
    long ans = 0;
    map<long,long>t;
    
    for(auto n: nums) t[gcd(n,k)]++;                              //fetch all gcd
    
    if(t.count(k)){                                               //case 1
      ans += ((nums.size()<<1) - t[k] - 1) * t[k] / 2; 
      t.erase(k);
    }
    if(t.count(1)) t.erase(1);                                    //case 2
    
    for(auto it = t.begin(); it != t.end(); it++){                                   //traversal through map
      if((it->first * it->first) % k == 0) ans += it->second*(it->second-1)/2;       //if gsd "good" for itself
      
      for(auto it2 = it ; ++it2 != t.end();)                                         //check with all greatest gsd
        if( (it->first * it2->first) % k == 0) ans += it->second * it2->second;
    }
    
    return ans;
        
    }
};