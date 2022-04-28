class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lo = 0
        hi = len(nums)-1
        # print(lo)
        # print(hi)
        if len(nums) == 0:
            # print(len(nums))
            return -1
        elif len(nums) == 1:
            if nums[0] == target:
                return 0
            else:
                return -1
        else:
            while lo<=hi:
                # print("lo",lo)
                # print("hi",hi)
                
                mid = round((lo + hi)/2)
                # print(mid)
                if (hi-lo) == 1:
                    if nums[hi] == target:
                        return hi
                    elif nums[lo] == target:
                        return lo
                    else:
                        return -1
                if nums[mid] == target:
                    return mid
                elif nums[mid] > target:
                    hi = mid
                elif nums[mid] < target:
                    lo = mid
            return -1
