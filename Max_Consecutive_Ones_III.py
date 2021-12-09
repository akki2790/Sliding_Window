Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array if you can flip at most k 0's.

Example 1:

Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
Output: 6
Explanation: [1,1,1,0,0,1,1,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.

Example 2:

Input: nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3
Output: 10
Explanation: [0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.

Approach: Sliding Window

In any sliding window based problem we have two pointers. One right pointer whose job is to expand the current window and then we have 
the left pointer whose job is to contract a given window. At any point in time only one of these pointers move and the other 
one remains fixed.

The solution is pretty intuitive. We keep expanding the window by moving the right pointer. When the window has reached the limit of 0's allowed,
we contract (if possible) and save the longest window till now.

Start at left = 0, right = 0, window_size = 0

We use the right pointer to expand the window until the window/subarray is desirable. i.e. number of 0's in the window are in the allowed range of [0, k].

Once we have a window which has more than the allowed number of 0's, we can move the left pointer ahead one by one until we encounter 0 on the left too. 
This step ensures we are throwing out the extra zero.

We can make this even more efficient.  Since we have to find the MAXIMUM window, we never reduce the size of the window. We either increase the size of the 
window or let it remain the same, but never reduce the size.

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = 0
        ln = len(nums)
        for right in range(ln):
            # if we include a 0 in the window, we reduce the vvalue of k by 1
            k -= 1 - nums[right] # this will do k-1 if nums[right] == 0, else k-0
            # a -ve k denotes we consumed all the ks and the window has more than allowed 0s
            # hence, we increment left pointer by 1
            if k < 0:
                # if the left element to be thrown out of the window is 0, we increase the k by 1
                k += 1 - nums[left]
                left += 1
	# Since, we never reduce the window beyond current max length, in the end, the window size will be the maximum it can be.
        return right - left + 1
