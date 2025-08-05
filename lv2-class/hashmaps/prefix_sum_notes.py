
'''
        0 1 2 3 4 5 6 
nums = [1,2,3,4,5,6,7] -> [1, 3, 6, 10, 15, 21, 28]
n = len(nums)

sum(1,3) = 2 + 3 + 4 = 9

def find_subarray_sum(nums, i, j): # o(n)
  current_sum = 0
  for k in range(i, j+1):
    current_sum += nums[k]
  return current_sum

number of queries = q

number of  queries = q
find_subarray_sum(1, 5)
find_subarray_sum(100, 120)
find_subarray_sum(45, 50)
find_subarray_sum(1, 5)
find_subarray_sum(1, 5)


time complexity: o(n) * o(q) = o(n * q)
              0  1  2   3   4  5   6
prefix_sum = [1, 3, 6, 10, 15, 21, 28]

sum(i,j)
sum(1,3) => prefix_sum[j] - prefix_sum[i-1] = 10 - 1 = 9 . t.c = o(1)
time complexity: o(n + q)

creating prefix_sum array:

method 1) in-place (saves memory)

def create_prefix_sum(arr):
  for i in range(1, len(arr)):
    arr[i] += arr[i-1]
  return arr
        i     j
        0 1 2 3 4 5 6
nums = [1,3,6,10,15,21,28]

arr[1] = arr[1] + arr[0] = 3
arr[2] = arr[2] + arr[1] = 6
...

space complexity: o(1)

def find_prefix_sum(prefix_arr, i, j):
  if i > 0:
    return prefix_arr[j] - prefix_arr[i-1]
  else:
    return prefix_arr[j]

method 2) creating a whole new array (adds memory, solves base case) -> padded prefix_sum

prefix_arr[j+1] - prefix_arr[i] 

prefix_sum = [0, 1, 3, 6, 10, 15, 21, 28]

space complexity: o(n)
prefix_sum = [0, 1, 3, 6, 10, 0, 0, 0]

----

def padded_prefix_sum(arr): 
  prefix_sum = [0] * (len(arr) + 1))
  for i in range(1, len(arr)):
    prefix_sum[i] = prefix_sum[i-1] + arr[i-1]
  return prefix_sum

nums = [1,2,3,4,5,6,7]
prefix_sum[0] = ---
prefix_sum[1] = prefix_sum[1-1] + arr[1-1] = 0 + 1 = 1
prefix_sum[2] = prefix_sum[2-1] + arr[2-1] = 1 + 2 = 3
prefix_sum[3] = prefix_sum[3-1] + arr[3-1] = 3 + 3 = 6
...

sum(i,j) = prefix_sum[j+1] - prefix_sum[i]

sum(1,3) = prefix_sum[4] - prefix_sum[1] = 10 - 1 = 9



'''

