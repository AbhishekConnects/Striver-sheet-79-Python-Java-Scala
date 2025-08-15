/*
 * Next Permutation Algorithm:
 * 
 * The algorithm finds the lexicographically next greater permutation.
 * If no such permutation exists, it rearranges to the smallest permutation.
 * 
 * Steps:
 * 1. Find the largest index i such that a[i] < a[i+1] (pivot)
 * 2. If no such i exists, the permutation is the last - reverse entire array
 * 3. Find the largest index j such that a[i] < a[j] (successor)
 * 4. Swap a[i] and a[j]
 * 5. Reverse the suffix starting at a[i+1]
 * 
 * Time: O(n), Space: O(1)
 */
object NextPermutation {
  def solve(a: Array[Int]): Unit = {
    val n = a.length
    
    // Step 1: Find pivot - rightmost element smaller than its next
    var i = n - 2
    while (i >= 0 && a(i) >= a(i + 1)) i -= 1
    
    if (i >= 0) {
      // Step 3: Find successor - smallest element greater than pivot
      var j = n - 1
      while (a(j) <= a(i)) j -= 1
      
      // Step 4: Swap pivot with successor
      val t = a(i); a(i) = a(j); a(j) = t
    }
    
    // Step 5: Reverse suffix to get next permutation
    var l = i + 1; var r = n - 1
    while (l < r) {
      val t = a(l); a(l) = a(r); a(r) = t
      l += 1; r -= 1
    }
  }
  
  def main(args: Array[String]): Unit = {
    // Example 1: {1,3,2} -> {2,1,3}
    val a1 = Array(1, 3, 2)
    solve(a1)
    val expected1 = Array(2, 1, 3)
    println(s"Example 1: ${a1.mkString(" ")} - ${if (a1.sameElements(expected1)) "✓" else "✗"}")
    
    // Example 2: {3,2,1} -> {1,2,3}
    val a2 = Array(3, 2, 1)
    solve(a2)
    val expected2 = Array(1, 2, 3)
    println(s"Example 2: ${a2.mkString(" ")} - ${if (a2.sameElements(expected2)) "✓" else "✗"}")
    
    // Test 3: {1,2,3} -> {1,3,2}
    val a3 = Array(1, 2, 3)
    solve(a3)
    val expected3 = Array(1, 3, 2)
    println(s"Test 3: ${a3.mkString(" ")} - ${if (a3.sameElements(expected3)) "✓" else "✗"}")
    
    // Test 4: {1} -> {1}
    val a4 = Array(1)
    solve(a4)
    val expected4 = Array(1)
    println(s"Test 4: ${a4.mkString(" ")} - ${if (a4.sameElements(expected4)) "✓" else "✗"}")
    
    // Test 5: {1,1,5} -> {1,5,1}
    val a5 = Array(1, 1, 5)
    solve(a5)
    val expected5 = Array(1, 5, 1)
    println(s"Test 5: ${a5.mkString(" ")} - ${if (a5.sameElements(expected5)) "✓" else "✗"}")
  }
}