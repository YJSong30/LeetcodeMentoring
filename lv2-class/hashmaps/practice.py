

'''
Create an algorithm to count the frequencies of a character using a hashmap. 
Then give me time complexity and space complexity of your algorithm.
Don't use Counter() or .get() methods
You're only given lowercase letters 

input: s
output: {'t': 4, 'h': 2, 'e': 7, 'r': 3, 'a': 2, 'm': 1, 'n': 2, 'y': 3, 'l': 1, 's': 4, 'i': 2}

hint:
- 7 lines of code
- to create a hashmap: hashmap = {} 
- to create key and value in a hashmap: hashmap[char] = 1
- how to handle a character that's already in the hashmap?

- constraints 
- only letters lowercase 
- no numbers

''' "worst case is 26"
s = "thereeareemanyyy!!@#12312312312!@!#letterssinthiss"
a = "aaaaaaaaaaaaaaaaaaaaaaa"

'''
{a: 1, b: 2, c: 3}
'''
class Leetcode:
  def count_frequency(self, s):
    hashmap = {}
    # loop over string 
    for letter in s:
      if letter not in hashmap: # if letter not in hashmap
        hashmap[letter] = 0
      hashmap[letter] += 1 

    for char in s:
      if char in hashmap:
        hashmap[char] += 1
      else:
        hashmap[char] = 1
    
    return hashmap


solution = Leetcode()
expected = {'t': 4, 'h': 2, 'e': 7, 'r': 3, 'a': 2, 'm': 1, 'n': 2, 'y': 3, 'l': 1, 's': 4, 'i': 2}
print(solution.count_frequency(s) == expected)
print('answer',solution.count_frequency(s))
print('a"s',solution.count_frequency(a))
