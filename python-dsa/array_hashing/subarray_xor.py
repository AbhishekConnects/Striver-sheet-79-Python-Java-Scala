def subarrays_with_xor(A, k):
    """
    Find total number of subarrays having bitwise XOR equal to k.
    
    Args:
        A: List of integers
        k: Target XOR value
    
    Returns:
        int: Count of subarrays with XOR equal to k
    """
    prefix_xor_count = {}
    prefix_xor = 0
    count = 0
    
    for num in A:
        prefix_xor ^= num
        
        # If prefix_xor equals k, subarray from start has XOR = k
        if prefix_xor == k:
            count += 1
        
        # Check if (prefix_xor ^ k) exists in map
        target = prefix_xor ^ k
        count += prefix_xor_count.get(target, 0)
        
        # Update count of current prefix_xor
        prefix_xor_count[prefix_xor] = prefix_xor_count.get(prefix_xor, 0) + 1
    
    return count


def test_subarrays_with_xor():
    # Test 1: [4, 2, 2, 6, 4], k = 6 -> 4
    A1 = [4, 2, 2, 6, 4]
    result1 = subarrays_with_xor(A1, 6)
    assert result1 == 4, f"Test 1 failed: got {result1}"
    print(f"Test 1: ✓ (result: {result1})")
    
    # Test 2: [5, 6, 7, 8, 9], k = 5 -> 2
    A2 = [5, 6, 7, 8, 9]
    result2 = subarrays_with_xor(A2, 5)
    assert result2 == 2, f"Test 2 failed: got {result2}"
    print(f"Test 2: ✓ (result: {result2})")
    
    # Test 3: [1, 1, 1], k = 0 -> 2 (subarrays: [1,1] at (0,1) and (1,2))
    A3 = [1, 1, 1]
    result3 = subarrays_with_xor(A3, 0)
    assert result3 == 2, f"Test 3 failed: got {result3}"
    print(f"Test 3: ✓ (result: {result3})")
    
    # Test 4: [1], k = 1 -> 1
    A4 = [1]
    result4 = subarrays_with_xor(A4, 1)
    assert result4 == 1, f"Test 4 failed: got {result4}"
    print(f"Test 4: ✓ (result: {result4})")
    
    print("All tests passed!")


if __name__ == "__main__":
    test_subarrays_with_xor()