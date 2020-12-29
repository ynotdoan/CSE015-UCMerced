
def Insert ():
  arr = []
  # loop asking for input
  while True:
    userInput = input ("Enter a new element for the set: ")
    arr.append (userInput)
    # loop to check to repeat and if input is valid
    while True:
      try:
        loop = input ("Enter one more element? [Y/N] ")
        if (loop == "N"):
          break
        elif (loop == "Y"):
          break
        print ("That is not a valid input. Try again: [Y/N] ")
      except Exception as e:
        print (e)
    if (loop == "N"):
      break
    elif (loop == "Y"):
      continue
  # makes arr a set and prints it
  res = set (arr)
  print (res)

# main
def main ():
  Insert ()

if __name__ == "__main__":
  main ()
