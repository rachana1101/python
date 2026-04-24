def two_sum(nums, target): 
    num_dict = {}
    for i, num in enumerate(nums):
        print(f"i: {i}, num: {num}")
        missing = target - nums[i]
        print(f"num: {num}, missing: {missing}", num_dict)
        if missing in num_dict:
            
            return [num_dict[missing],i]
        num_dict[num] = i

if __name__ == "__main__":
    nums = [2, 7, 11, 15]
    target = 9
    print(two_sum(nums, target))
