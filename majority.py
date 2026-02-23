def majority_element(nums):
    freq = {}
    
    for num in nums:
        freq[num] = freq.get(num, 0) + 1
    
    for key, value in freq.items():
        if value > len(nums) // 2:
            return key

print(majority_element([2,2,1,1,2,2,2]))