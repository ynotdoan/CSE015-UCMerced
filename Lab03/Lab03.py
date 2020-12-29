from logic import TruthTable

# tautology: (-p and (p or q)) -> q
#            ((p1 or p2 or p3) -> q) <-> ((p1 -> q) and (p2 -> q) and (p3 -> q))
# contradiction: p and -p
# contingency: (p -> (q or r)) -> (-q or p)


def Table(arr):
  t1 = TruthTable(arr)
  # displays truth table as table
  t1.display()
  print()

  a = t1.table
  # prints t1 data as array
  print(a)
  print()

  res = []
  asize = len(a)
  # loop to print out the result of each proposition
  for i in range(asize):
    print(a[i][1])
    # places each num in column 1 into array
    res.append(a[i][1])

  print()

  # checks if elements in res are tautology, contradiction, or contingency
  if (res.count([1]) == asize):
    print("This is a tautology")
  elif (res.count([0]) == asize):
    print("This is a contradiction")
  else:
    print("This is a contingency")

# main


def main():
  # gets proposition from user
  userInput = input("Enter a proposition: ")

  # adding userInput to arr
  arr = []
  arr.append(userInput)

  # calling Table func
  Table(arr)


if __name__ == "__main__":
  main()
