
# functions/ sets
A = set ({"a", "b", "c", "d", "e"})
B = set ({1, 2, 3, 4, 5, 6, 7, 8, 9, 10})
f = set ({("a", 2), ("b", 4), ("c", 6), ("d", 8)})
g = set ({("b", 4), ("c", 6), ("a", 2), ("d", 8)})
h = set ({(4, "bear"), (1, "cat"), (10, "bird"), (8, "duck")})

def equal_func (f, g):
  print ("Function f: ")
  print (f)
  print ("Function g: ")
  print (g)

  # checks is functions f and g are equal
  if f == g:
    return True
  else:
    return False

check1 = equal_func (f, g)
if check1 == True:
  print ("Functions f and g are equal. ")
else:
  print ("Functions f and g are not equal. ")
print ()

def partial_func (A, f):
  print ("Domain A: ")
  print (A)
  print ("Function f: ")
  print (f)

  # length of set A
  x = len (A)
  # loop for elements in function f
  for i in f:
    a = i[0]

  # length of elements
  y = len(a)
  counter = 0
  # checks count of element
  while counter != y:
    counter = counter + 1

  if (counter <= x):
    return True
  else:
    return False

check2 = partial_func (A, f)
if check2 == True:
  print ("Functions f is a partial function of domain A. ")
else:
  print ("Functions f is not a partial function of domain A. ")
print ()

def composite_func (f, h):
  a = set ({})
  # loop to check elements in functions f and h
  for x in f:
    for y in h:
      # checks for tuples that are equal and set them to each other
      if x[1] == y[0]:
        a.add ((x[0], y[1]))

  print (f)
  print (h)
  return a

print ("Composite function: ")
print (composite_func (f, h))

# A = {"dog", "cat", "fish"}
# B = {1, 2}
# f = {("cat", 2), ("dog", 1), ("fish", 1)}

# for i in f:
#     print (i)
