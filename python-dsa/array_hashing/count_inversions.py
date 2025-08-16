def count_inversions_brute(nums):
    """
    Count inversions using brute force approach.
    
    Approach: Check all pairs (i, j) where i < j
    - If nums[i] > nums[j], it's an inversion
    
    Time Complexity: O(n²)
    Space Complexity: O(1)
    
    Args:
        nums: List of integers
    
    Returns:
        int: Number of inversions
    """
    count = 0
    n = len(nums)
    
    for i in range(n):
        for j in range(i + 1, n):
            if nums[i] > nums[j]:
                count += 1
    
    return count


def count_inversions_merge_sort(nums):
    """
    Count inversions using merge sort approach (optimal).
    
    Approach: During merge step of merge sort, count inversions
    - When element from right array is smaller, it forms inversions
    - with all remaining elements in left array
    
    Time Complexity: O(n log n)
    Space Complexity: O(n)
    
    Args:
        nums: List of integers
    
    Returns:
        int: Number of inversions
    """
    def merge_and_count(arr, temp, left, mid, right):
        i, j, k = left, mid + 1, left
        inv_count = 0
        
        # Merge and count inversions
        while i <= mid and j <= right:
            if arr[i] <= arr[j]:
                temp[k] = arr[i]
                i += 1
            else:
                temp[k] = arr[j]
                # All elements from i to mid are greater than arr[j]
                inv_count += (mid - i + 1)
                j += 1
            k += 1
        
        # Copy remaining elements
        while i <= mid:
            temp[k] = arr[i]
            i += 1
            k += 1
        
        while j <= right:
            temp[k] = arr[j]
            j += 1
            k += 1
        
        # Copy back to original array
        for i in range(left, right + 1):
            arr[i] = temp[i]
        
        return inv_count
    
    def merge_sort_and_count(arr, temp, left, right):
        inv_count = 0
        if left < right:
            mid = (left + right) // 2
            
            inv_count += merge_sort_and_count(arr, temp, left, mid)
            inv_count += merge_sort_and_count(arr, temp, mid + 1, right)
            inv_count += merge_and_count(arr, temp, left, mid, right)
        
        return inv_count
    
    # Create copy to avoid modifying original array
    arr_copy = nums.copy()
    temp = [0] * len(nums)
    return merge_sort_and_count(arr_copy, temp, 0, len(nums) - 1)


def test_count_inversions():
    # Test 1: [2, 4, 1, 3, 5] -> 3 inversions: (2,1), (4,1), (4,3)
    nums1 = [2, 4, 1, 3, 5]
    result1_brute = count_inversions_brute(nums1)
    result1_merge = count_inversions_merge_sort(nums1)
    assert result1_brute == 3, f"Brute test 1 failed: got {result1_brute}"
    assert result1_merge == 3, f"Merge test 1 failed: got {result1_merge}"
    print(f"Test 1: ✓ (brute: {result1_brute}, merge: {result1_merge})")
    
    # Test 2: [2, 3, 4, 5, 6] -> 0 inversions (sorted)
    nums2 = [2, 3, 4, 5, 6]
    result2_brute = count_inversions_brute(nums2)
    result2_merge = count_inversions_merge_sort(nums2)
    assert result2_brute == 0, f"Brute test 2 failed: got {result2_brute}"
    assert result2_merge == 0, f"Merge test 2 failed: got {result2_merge}"
    print(f"Test 2: ✓ (brute: {result2_brute}, merge: {result2_merge})")
    
    # Test 3: [5, 4, 3, 2, 1] -> 10 inversions (reverse sorted)
    nums3 = [5, 4, 3, 2, 1]
    result3_brute = count_inversions_brute(nums3)
    result3_merge = count_inversions_merge_sort(nums3)
    assert result3_brute == 10, f"Brute test 3 failed: got {result3_brute}"
    assert result3_merge == 10, f"Merge test 3 failed: got {result3_merge}"
    print(f"Test 3: ✓ (brute: {result3_brute}, merge: {result3_merge})")
    
    # Test 4: [1, 20, 6, 4, 5] -> 5 inversions
    nums4 = [1, 20, 6, 4, 5]
    result4_brute = count_inversions_brute(nums4)
    result4_merge = count_inversions_merge_sort(nums4)
    assert result4_brute == 5, f"Brute test 4 failed: got {result4_brute}"
    assert result4_merge == 5, f"Merge test 4 failed: got {result4_merge}"
    print(f"Test 4: ✓ (brute: {result4_brute}, merge: {result4_merge})")
    
    print("All tests passed!")


if __name__ == "__main__":
    test_count_inversions()