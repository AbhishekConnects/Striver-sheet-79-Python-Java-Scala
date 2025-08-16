def max_product_subarray(nums):
    """
    Find maximum product of contiguous subarray using Kadane's algorithm variant.
    
    Approach: Track both max and min products at each position
    - Negative numbers can make min become max when multiplied
    - At each step, consider: current element, max*current, min*current
    
    Time Complexity: O(n)
    Space Complexity: O(1)
    
    Args:
        nums: List of integers
    
    Returns:
        int: Maximum product of subarray
    """
    if not nums:
        return 0
    
    max_product = min_product = result = nums[0]
    
    for i in range(1, len(nums)):
        current = nums[i]
        
        # Store max_product before updating (needed for min_product calculation)
        temp_max = max_product
        
        # Update max and min products
        max_product = max(current, max_product * current, min_product * current)
        min_product = min(current, temp_max * current, min_product * current)
        
        # Update global result
        result = max(result, max_product)
    
    return result


def max_product_subarray_brute(nums):
    """
    Brute force approach - check all subarrays.
    
    Time Complexity: O(n²)
    Space Complexity: O(1)
    
    Args:
        nums: List of integers
    
    Returns:
        int: Maximum product of subarray
    """
    if not nums:
        return 0
    
    max_product = nums[0]
    n = len(nums)
    
    for i in range(n):
        current_product = 1
        for j in range(i, n):
            current_product *= nums[j]
            max_product = max(max_product, current_product)
    
    return max_product


def max_product_subarray_prefix_suffix(nums):
    """
    Alternative approach using prefix and suffix products.
    
    Approach: Calculate products from left and right
    - Reset to 1 when encountering 0
    - Maximum of all prefix/suffix products is the answer
    
    Time Complexity: O(n)
    Space Complexity: O(1)
    
    Args:
        nums: List of integers
    
    Returns:
        int: Maximum product of subarray
    """
    if not nums:
        return 0
    
    n = len(nums)
    prefix = suffix = 1
    max_product = float('-inf')
    
    for i in range(n):
        # Reset to 1 if becomes 0
        if prefix == 0:
            prefix = 1
        if suffix == 0:
            suffix = 1
        
        prefix *= nums[i]
        suffix *= nums[n - 1 - i]
        
        max_product = max(max_product, max(prefix, suffix))
    
    return max_product


def test_max_product_subarray():
    # Test 1: [2, 3, -2, 4] -> 6 (subarray [2, 3])
    nums1 = [2, 3, -2, 4]
    result1 = max_product_subarray(nums1)
    result1_brute = max_product_subarray_brute(nums1)
    result1_prefix = max_product_subarray_prefix_suffix(nums1)
    assert result1 == 6, f"Kadane test 1 failed: got {result1}"
    assert result1_brute == 6, f"Brute test 1 failed: got {result1_brute}"
    assert result1_prefix == 6, f"Prefix test 1 failed: got {result1_prefix}"
    print(f"Test 1: ✓ (kadane: {result1}, brute: {result1_brute}, prefix: {result1_prefix})")
    
    # Test 2: [-2, 0, -1] -> 0
    nums2 = [-2, 0, -1]
    result2 = max_product_subarray(nums2)
    result2_brute = max_product_subarray_brute(nums2)
    result2_prefix = max_product_subarray_prefix_suffix(nums2)
    assert result2 == 0, f"Kadane test 2 failed: got {result2}"
    assert result2_brute == 0, f"Brute test 2 failed: got {result2_brute}"
    assert result2_prefix == 0, f"Prefix test 2 failed: got {result2_prefix}"
    print(f"Test 2: ✓ (kadane: {result2}, brute: {result2_brute}, prefix: {result2_prefix})")
    
    # Test 3: [-2, 3, -4] -> 24 (entire array)
    nums3 = [-2, 3, -4]
    result3 = max_product_subarray(nums3)
    result3_brute = max_product_subarray_brute(nums3)
    result3_prefix = max_product_subarray_prefix_suffix(nums3)
    assert result3 == 24, f"Kadane test 3 failed: got {result3}"
    assert result3_brute == 24, f"Brute test 3 failed: got {result3_brute}"
    assert result3_prefix == 24, f"Prefix test 3 failed: got {result3_prefix}"
    print(f"Test 3: ✓ (kadane: {result3}, brute: {result3_brute}, prefix: {result3_prefix})")
    
    # Test 4: [0, 2] -> 2
    nums4 = [0, 2]
    result4 = max_product_subarray(nums4)
    result4_brute = max_product_subarray_brute(nums4)
    result4_prefix = max_product_subarray_prefix_suffix(nums4)
    assert result4 == 2, f"Kadane test 4 failed: got {result4}"
    assert result4_brute == 2, f"Brute test 4 failed: got {result4_brute}"
    assert result4_prefix == 2, f"Prefix test 4 failed: got {result4_prefix}"
    print(f"Test 4: ✓ (kadane: {result4}, brute: {result4_brute}, prefix: {result4_prefix})")
    
    print("All tests passed!")


if __name__ == "__main__":
    test_max_product_subarray()