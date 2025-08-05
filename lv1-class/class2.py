
nums = [2, 7, 11, 15]


'1) iterating through single element in array. print each  number'

for i in nums:
    print(i)



'2) iterating with index. print (index, number)'

for i in range(0,len(nums),1): # for i in range(len(nums))
    print("Value:"+ i + "index" +nums[i]) # print((index, number)) <- tuple 

'''''''''

3) nested for loops
        0  1   2   3
nums = [2, 7, 11, 15]

(2,2)
(2,7)
(2,11)
(2,15)
(7,7)
(7,2)
(7,11)

# print all pairs of numbers including duplicates
''''''''''''
for i in range(start, stop, step)
len(nums) -> 4, but len(nums) excludes last index

for num1 in nums:
    for num2 in nums:
        print((num1, num2))

follow up: what's another way to do this using just values?

for i in range(len(nums)):
    for j in range(len(nums)):
        print((nums[i], nums[j]))

        
follow up: how would we remove duplicates? we don't want (7,2) if we have (2,7). also avoid identical values such as (2,2) 
                   i
                      j
        0  1   2   3
nums = [2, 7, 11, 15]
i = 0: (2,7), (2,11), (2, 15)
i = 1: (7,11), (7,15)
i = 2: (11,15)

 for i in range(len(nums)): 
    for j in range(i+1,len(nums)): 
        print((nums[i],nums[j]))


4) Two Sum

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]

Constraints:

2 <= nums.length <= 10^4
-10^9 <= nums[i] <= 10^9
-10^9 <= target <= 10^9
Only one valid answer exists.



for i in range(len(nums)): # t.c : o(n)
    for j in range(i+1,len(nums)): # t.c : o(n)
        if (nums[i] + nums[j] == target):
            print([i,j])
 
  
Time complexity:

Best Case: 
nums = [4, 5, 1, 2, 3, 6, 7]
target = 9

t.c = o(1)

Worst Case:
nums = [1, 2, 3, 4, 5, 6, 7]
target = 13

t.c = o(n^2)


217. Contains Duplicate

Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.


Example 1:

Input: nums = [1,2,3,1]

Output: true

Explanation:

The element 1 occurs at the indices 0 and 3.

Example 2:

Input: nums = [1,2,3,4]

Output: false

Explanation:

All elements are distinct.

Example 3:

Input: nums = [1,1,1,3,3,4,3,2,4,2]

Output: true



for i in range(len(nums)): 
    for j in range(i+1,len(nums)):
        if(nums[i]==nums[j]): 
            return True 

return False 

Time complexity Best case: o(1)

Time complexity Average/Worst case:o(n^2)





'''