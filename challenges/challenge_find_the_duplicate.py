def find_duplicate(nums):
    if nums and len(nums) > 1:
        set_ = set()
        for num in nums:
            if isinstance(num, str) or num < 0:
                return False
            if num in set_:
                return num
            set_.add(num)    
        return False
    return False    