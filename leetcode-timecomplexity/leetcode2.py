#Given a non-empty array of integers, every element appears twice except for one. Find that single one.
def singleNumber(nums):
    duplicates = set()
    for num in nums:
        if num not in duplicates:
            duplicates.add(num)
        else:
            duplicates.remove(num)
    return duplicates.pop()

#The time complexity would be O(n) because it is directly proportional to the size of the input.
