object MajorityElementII {
  // Find elements appearing more than n/3 times using Boyer-Moore Voting Algorithm
  def majorityElement(nums: Array[Int]): List[Int] = {
    var candidate1 = 0; var candidate2 = 0
    var count1 = 0; var count2 = 0
    
    // Phase 1: Find potential candidates (at most 2 elements can appear > n/3 times)
    for (num <- nums) {
      if (num == candidate1) count1 += 1
      else if (num == candidate2) count2 += 1
      else if (count1 == 0) { candidate1 = num; count1 = 1 }
      else if (count2 == 0) { candidate2 = num; count2 = 1 }
      else { count1 -= 1; count2 -= 1 }
    }
    
    // Phase 2: Verify candidates actually appear > n/3 times
    count1 = 0; count2 = 0
    for (num <- nums) {
      if (num == candidate1) count1 += 1
      else if (num == candidate2) count2 += 1
    }
    
    val threshold = nums.length / 3
    var result = List[Int]()
    if (count1 > threshold) result = candidate1 :: result
    if (count2 > threshold && candidate2 != candidate1) result = candidate2 :: result
    result
  }
  
  def main(args: Array[String]): Unit = {
    // Test 1: [1, 2, 1, 1, 3, 2] -> [1]
    val nums1 = Array(1, 2, 1, 1, 3, 2)
    val result1 = majorityElement(nums1)
    assert(result1.toSet == Set(1), s"Test 1 failed: got $result1")
    println(s"Test 1: ✓ (result: ${result1.mkString("[", ", ", "]")})")
    
    // Test 2: [1, 2, 1, 1, 3, 2, 2] -> [1, 2]
    val nums2 = Array(1, 2, 1, 1, 3, 2, 2)
    val result2 = majorityElement(nums2)
    assert(result2.toSet == Set(1, 2), s"Test 2 failed: got $result2")
    println(s"Test 2: ✓ (result: ${result2.mkString("[", ", ", "]")})")
    
    // Test 3: [3, 2, 3] -> [3]
    val nums3 = Array(3, 2, 3)
    val result3 = majorityElement(nums3)
    assert(result3.toSet == Set(3), s"Test 3 failed: got $result3")
    println(s"Test 3: ✓ (result: ${result3.mkString("[", ", ", "]")})")
    
    // Test 4: [1] -> [1]
    val nums4 = Array(1)
    val result4 = majorityElement(nums4)
    assert(result4.toSet == Set(1), s"Test 4 failed: got $result4")
    println(s"Test 4: ✓ (result: ${result4.mkString("[", ", ", "]")})")
    
    // Test 5: [1, 2] -> [1, 2] (both appear > n/3 = 0 times)
    val nums5 = Array(1, 2)
    val result5 = majorityElement(nums5)
    assert(result5.toSet == Set(1, 2), s"Test 5 failed: got $result5")
    println(s"Test 5: ✓ (result: ${result5.mkString("[", ", ", "]")})")
    
    println("All tests passed!")
  }
}