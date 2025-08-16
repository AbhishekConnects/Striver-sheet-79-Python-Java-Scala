def find_duplicate_missing(nums):
    """
    Find duplicate and missing number in array [1, n].
    
    Approach: Use XOR properties
    - XOR all array elements with numbers 1 to n
    - Result will be duplicate ^ missing
    - Use rightmost set bit to separate them
    
    Time Complexity: O(n)
    Space Complexity: O(1)
    
    Args:
        nums: List of integers from [1, n] with one duplicate and one missing
    
    Returns:
        List[int]: [duplicate, missing]
    """
    n = len(nums)
    xor_all = 0
    
    # XOR all array elements and numbers 1 to n
    for i in range(n):
        xor_all ^= nums[i] ^ (i + 1)
    
    # Find rightmost set bit
    rightmost_bit = xor_all & -xor_all
    
    # Separate numbers into two groups based on rightmost bit
    group1 = group2 = 0
    
    for num in nums:
        if num & rightmost_bit:
            group1 ^= num
        else:
            group2 ^= num
    
    for i in range(1, n + 1):
        if i & rightmost_bit:
            group1 ^= i
        else:
            group2 ^= i
    
    # Determine which is duplicate by checking presence in array
    duplicate = group1 if group1 in nums else group2
    missing = group2 if duplicate == group1 else group1
    
    return [duplicate, missing]


def find_duplicate_missing_hash(nums):
    """
    Alternative approach using hash set.
    
    Time Complexity: O(n)
    Space Complexity: O(n)
    
    Args:
        nums: List of integers from [1, n] with one duplicate and one missing
    
    Returns:
        List[int]: [duplicate, missing]
    """
    n = len(nums)
    seen = set()
    duplicate = -1
    
    # Find duplicate
    for num in nums:
        if num in seen:
            duplicate = num
        seen.add(num)
    
    # Find missing
    for i in range(1, n + 1):
        if i not in seen:
            missing = i
            break
    
    return [duplicate, missing]


def test_find_duplicate_missing():
    # Test 1: [3, 1, 2, 5, 3] -> [3, 4]
    nums1 = [3, 1, 2, 5, 3]
    result1 = find_duplicate_missing(nums1)
    assert result1 == [3, 4], f"Test 1 failed: got {result1}"
    print(f"Test 1: ✓ (result: {result1})")
    
    # Test 2: [1, 1] -> [1, 2]
    nums2 = [1, 1]
    result2 = find_duplicate_missing(nums2)
    assert result2 == [1, 2], f"Test 2 failed: got {result2}"
    print(f"Test 2: ✓ (result: {result2})")
    
    # Test 3: [2, 2, 3, 4] -> [2, 1]
    nums3 = [2, 2, 3, 4]
    result3 = find_duplicate_missing(nums3)
    assert result3 == [2, 1], f"Test 3 failed: got {result3}"
    print(f"Test 3: ✓ (result: {result3})")
    
    # Test hash approach
    result1_hash = find_duplicate_missing_hash(nums1)
    assert result1_hash == [3, 4], f"Hash test failed: got {result1_hash}"
    print(f"Hash approach: ✓ (result: {result1_hash})")
    
    print("All tests passed!")


if __name__ == "__main__":
    test_find_duplicate_missing()