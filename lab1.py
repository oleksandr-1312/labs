def is_subarray(nums1, nums2):
    if len(nums1) > len(nums2):
        return False

    for i in range(len(nums2) - len(nums1) + 1):
        if nums2[i : i + len(nums1)] == nums1:
            return True
    return False

