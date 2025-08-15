//The algorithm runs in O(n) time and O(1) space, making it optimal for finding the maximum contiguous subarray sum.

object KadaneAlgorithm {
  // Find maximum sum of contiguous subarray using Kadane's Algorithm
  def maxSubarraySum(nums: Array[Int]): Int = {
    var maxSum = nums(0)     // Global maximum sum found so far
    var currentSum = nums(0) // Current subarray sum ending at current position
    
    // Iterate through array starting from second element
    for (i <- 1 until nums.length) {
      // Either extend current subarray or start new one from current element
      currentSum = math.max(nums(i), currentSum + nums(i))
      // Update global maximum if current sum is larger
      maxSum = math.max(maxSum, currentSum)
    }
    maxSum
  }
  
  def main(args: Array[String]): Unit = {
    // Test 1: Mixed positive and negative numbers
    val nums1 = Array(2, 3, 5, -2, 7, -4)
    val result1 = maxSubarraySum(nums1)
    assert(result1 == 15, s"Test 1 failed: expected 15, got $result1")
    println(s"Test 1: ✓ (result: $result1)")
    
    // Test 2: All negative numbers
    val nums2 = Array(-2, -3, -7, -2, -10, -4)
    val result2 = maxSubarraySum(nums2)
    assert(result2 == -2, s"Test 2 failed: expected -2, got $result2")
    println(s"Test 2: ✓ (result: $result2)")
    
    // Test 3: Single element
    val nums3 = Array(5)
    val result3 = maxSubarraySum(nums3)
    assert(result3 == 5, s"Test 3 failed: expected 5, got $result3")
    println(s"Test 3: ✓ (result: $result3)")
    
    // Test 4: Classic example
    val nums4 = Array(-2, 1, -3, 4, -1, 2, 1, -5, 4)
    val result4 = maxSubarraySum(nums4)
    assert(result4 == 6, s"Test 4 failed: expected 6, got $result4")
    println(s"Test 4: ✓ (result: $result4)")
    
    println("All tests passed!")
  }
}