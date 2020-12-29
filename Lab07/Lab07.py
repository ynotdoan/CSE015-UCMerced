
# Recursively defined functions
# asks user to input an int for n
n = int(input("Enter a num for n: "))

# func compute_f returns value for f(n) for given n


def compute_f(n):
  # if user inputs 0, compute_f returns 2
  if (n == 0):
    return 2
  # if user does not enter 0, compute_f recursively calls itself to return f(n - 1) + 2
  else:
    return compute_f(n - 1) + 2


# answer
print(compute_f(n))

# Counting the number of occurrences of an element in a list
# L given from lab07 pdf
L = [4, 5, 9, 7, 7, 1, 9, 7, 2]

# func count_instances takes in list L and num i


def count_instances(L, i):
  # if L is empty, count_instances returns 0
  if (L == []):
    return 0
  # if first element in L is equal to i, count_instances returns count_instances + 1
  elif (L[0] == i):
    return 1 + count_instances(L[1:], i)
  # if first two conditions not met, returns count_instances with the tail L and i
  else:
    return count_instances(L[1:], i)


# tests
print(f"occurrences of 4: {count_instances (L, 4)}")
print(f"occurrences of 7: {count_instances (L, 7)}")
print(f"occurrences of 9: {count_instances (L, 9)}")
print(f"occurrences of 0: {count_instances (L, 0)}")
print(f"occurrences of 5: {count_instances (L, 5)}")
