print ("Please enter 10 integers: ")

largest = None
i = 0

while (i < 10 ):
  num = int (input ("* "))
  if (num % 2) != 0 and (not largest or num > largest):
    largest = num
  i = i + 1

if (largest == None):
  print("You didn't enter any odd numbers")
else:
  print("Your largest odd number was:", largest)
