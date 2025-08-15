object ThreeSum {
  // Find all unique triplets that sum to zero
  def threeSum(nums: Array[Int]): List[List[Int]] = {
    // Sort array to enable two-pointer technique and skip duplicates
    val sorted = nums.sorted
    
    // For each element as first element of triplet
    (for {
      // Skip last 2 elements (need at least 3 for triplet)
      // Skip duplicates: only process if first occurrence
      i <- sorted.indices.dropRight(2) if i == 0 || sorted(i) != sorted(i-1)
      triplet <- findTriplets(sorted, i)
    } yield triplet).toList
  }
  
  // Find triplets starting with element at index i using two-pointer technique
  private def findTriplets(arr: Array[Int], i: Int): List[List[Int]] = {
    var left = i + 1          // Left pointer starts after current element
    var right = arr.length - 1 // Right pointer starts at end
    var result = List[List[Int]]()
    
    while (left < right) {
      val sum = arr(i) + arr(left) + arr(right)
      if (sum == 0) {
        // Found valid triplet
        result = List(arr(i), arr(left), arr(right)) :: result
        // Skip duplicates on both sides
        while (left < right && arr(left) == arr(left + 1)) left += 1
        while (left < right && arr(right) == arr(right - 1)) right -= 1
        left += 1
        right -= 1
      } else if (sum < 0) left += 1  // Sum too small, move left pointer right
      else right -= 1                // Sum too large, move right pointer left
    }
    result
  }
  
  def main(args: Array[String]): Unit = {
    // Test 1
    val nums1 = Array(-1, 0, 1, 2, -1, -4)
    val result1 = threeSum(nums1)
    val expected1 = List(List(-1, -1, 2), List(-1, 0, 1))
    assert(result1.toSet == expected1.toSet, s"Test 1 failed: got $result1")
    println(s"Test 1: ✓")
    
    // Test 2
    val nums2 = Array(-1, 0, 1, 0)
    val result2 = threeSum(nums2)
    val expected2 = List(List(-1, 0, 1))
    assert(result2.toSet == expected2.toSet, s"Test 2 failed: got $result2")
    println(s"Test 2: ✓")
    
    // Test 3: No solution
    val nums3 = Array(0, 1, 1)
    val result3 = threeSum(nums3)
    assert(result3.isEmpty, s"Test 3 failed: got $result3")
    println(s"Test 3: ✓")
    
    // Test 4: All zeros
    val nums4 = Array(0, 0, 0)
    val result4 = threeSum(nums4)
    val expected4 = List(List(0, 0, 0))
    assert(result4 == expected4, s"Test 4 failed: got $result4")
    println(s"Test 4: ✓")
    
    println("All tests passed!")
  }
}