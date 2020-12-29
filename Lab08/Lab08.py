
import random, time

def gen_random_list(n):
  '''
  Generates a random list of n non-negative integers and returns list.
  '''
  assert(n > 0)
  l = [random.randint(0, 10*n) for i in range(n)]
  return l

def linear_search(s, k):
  '''
  Determines if k is in list s using linear search algorithm.
  '''
  # loop runs through list s and finds if k matches any indices and returns i
  for i in range(len(s)):
    if (s[i] == k):
      return i
  # if none found, returns -1
  return -1

def binary_search(s, k):
  '''
  Determines if k is in list s using binary search algorithm.
  '''
  x = 0
  y = len(s)
  while (x < y):
    # finds middle of the list
    mid = (x + y) // 2
    # compares k to middle of list and deletes half of list that k is not in
    if (k > s[mid]):
      x = mid
    elif (k < s[mid]):
      y = mid
    elif (k == s[mid]):
      return mid
  # if none found, returns -1
  return -1

# linear search timer
for i in range(9):
  a = gen_random_list(10**i)
  # timer
  start_time = time.perf_counter()
  linear_search(a, -1)
  spent_time = (time.perf_counter() - start_time)
  print (f"{i}. Time spent calling linear_search(): {spent_time} s")
  
print ()

# binary seach timer
for i in range(9):
  b = gen_random_list(10**i)
  # timer
  start_time = time.perf_counter()
  binary_search(b, -1)
  spent_time = time.perf_counter() - start_time
  print (f"{i}. Time spent calling binary_search(): {spent_time} s")
