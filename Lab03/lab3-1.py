# Using TruthTable() from logic.py
from logic import TruthTable

# example proposition

myTable = TruthTable(['a -> b'])
myTable.display()  # equivalent to TruthTable(['a ->b']).display


a = myTable.table
print(a[0][1])
print(len(a))


##-------- Getting an inout from user for the truthtable -----------------##

# when getting an input from user, append the proposition enter by user into
# an empty list and then pass the list as argument to the TruthTable() method

list1 = []
expr = input("Enter an expression:")
list1.append(expr)
myTbl = TruthTable(list1)
myTbl.display()

