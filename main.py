# This assignment will be to build a function that mimics the slice operator. Instead of the slice notation with
#  the square brackets, your slice function will be called as a function with four parameters:

# 1. iter_obj: The iterable object that will be split. (Required)
# 2. start: The start index. Negative numbers are valid. Default=1
# 3. stop: The stop index. Remember that the slice will end before the stop index. Default = None
# 4. step: The step direction and magnitude as a positive or negative integer. Default=1

# The signature of the function should be:

# def slice(iter_obj, start=0, stop=None, step=1):

#   Here are some examples of the slice function:

# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# output = slice(nums, 2, -2)

# print(output)

# # Output
# [3, 4, 5, 6, 7]

# ## Example 2
# print( slice(nums, stop = 4) )

# # Output
# [1, 2, 3, 4]

# ## Example
# print( slice(nums, step=-1) )

# # Output
# [9, 8, 7, 6, 5, 4, 3, 2, 1]


nums =[1,2,3,4,5,6,7,8,9]

def slice(itter, start = None, stop = None, step = 1):
  list = []

  if step > 0:
    if start == None:
      start = 0
    if stop == None:
      stop = len(itter)

  if step < 0:
    if start == None:
      start = -1
    if stop == None:
      stop = -len(itter) -1

  if start < 0:
    start = len(itter) + start
  if stop < 0:
    stop = len(itter) + stop

  for i in range(start, stop, step):
      list.append(itter[i])
     
  return list

print(nums[2:-2])
print(slice(nums, 2, -2))

print(nums[:4])
print(slice(nums, stop = 4))

print(nums[::-1])
print(slice(nums, step=-1))

print(nums[-2:1:-1])
print(slice(nums, -2, 1, -1))

print(nums[:1:-1])
print(slice(nums, stop=1,step=-1))
      