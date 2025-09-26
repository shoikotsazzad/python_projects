high_income = False
good_credit = True
student = True

#Here we used -- or, and, not operator
#not operator  is when something is false
if(high_income or good_credit) and not student: 
    print("Eligible")
else: 
    print("Not Eligible")