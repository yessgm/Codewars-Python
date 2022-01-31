def even_last(nums): 
    return sum([nums[i] for i in range(0,len(nums),2)]) * nums[-1] if nums != [] else 0