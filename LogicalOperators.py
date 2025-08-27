# In python && and || and ! is just written as 'and' and 'or' and 'not'
highIncome = False
goodCredit = False
if highIncome and goodCredit:
    print("Eligible for loan")
elif highIncome or goodCredit:
    print("Under process")
# elif highIncome or not goodCredit:
#    print("Under process")
else:
    print("Not eligible")
