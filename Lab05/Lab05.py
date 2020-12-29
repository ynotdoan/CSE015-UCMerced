
def is_a_graph (A, B, f):
  # loop to run through elements 
  for element in f:
    a = element[0]
    for other in f:
      if (other != element):
        prime = other[0]
        # checks if elements repeat
        if (a == prime):
          return False

  return True

def is_surjective (A, B, f):

  a = set ()
  b = set ()


  for item in f:
    # checks if items in f are from A and B
    if item[0] not in A:
      return False
    if item [1] not in B:
      return False
    # looks for repeating elements in A
    for i in A:
      if item[0] == i:
        if item [0] not in a:
          a.add(item[0])
          b.add(item[1])
        else:
          return False
  # checks if A values are in f
  if a != A:
    return False
  # checks if B values are in f
  for item in B:
      if item not in b:
        return False
  return True

# main
def main ():
  A = set (["cat", "bear", "seal", "duck"])
  B = set ([1, 2, 3, 4])
  f = set ([("cat", 1), ("bear", 2), ("seal", 3), ("duck", 4)])

  print ("Domain A: ")
  print (A)
  print ("Domain B: ")
  print (B)
  print ("Graph of the function: ")
  print (f)
  print ()

  is_a_graph (A, B, f)

  print ("f: A -> B:")
  # checks to see if f is a graph
  check_graph = is_a_graph (A, B, f)
  if check_graph == True:
    print ("Function f is a graph ")
  else:
    print ("Function f is not a graph")

  is_surjective (A, B, f)

  print ("f: A X B:")
  # checks to see if f is surjective
  check_sur = is_surjective (A, B, f)
  if check_sur == True:
    print ("Function f is surjective ")
  else:
    print ("Function f is not surjective")

if __name__ == "__main__":
  main ()