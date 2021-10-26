# Given an integer array nums and two integers k and t, return true if there are two distinct indices i and j in the array such that abs(nums[i] - nums[j]) <= t and abs(i - j) <= k.

# Input: nums = [1,2,3,1], k = 3, t = 0
# Output: true

# Input: nums = [1,0,1,1], k = 1, t = 2
# Output: true

class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        # using buckets
        if k<0 or t<0:
            return False
        bucket_size=t+1
        
        m_buckets={}
        
        for i in range(len(nums)):
            
            m=nums[i]//bucket_size
            
            if m in m_buckets:
                return True
            
            elif (m-1 in m_buckets) and abs(nums[i]-m_buckets[m-1])<bucket_size:
                return True
            
            elif (m+1 in m_buckets) and abs(nums[i]-m_buckets[m+1])<bucket_size:
                return True
            
            m_buckets[m]=nums[i]
            
            #removing the bucket corresponding to number out of our k sized window
            if i>=k:
		del m_buckets[nums[i-k]/bucket_size]
            
	return False
