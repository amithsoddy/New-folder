height=float(input("enter a height"))
weight=float(input("enter a weight"))
bmi=weight/(height*height)
print(bmi)
if bmi<=18.4:
    print("your under weight")
elif bmi<=24.9:
    print("your healhthy")
elif bmi<=29.9:
      print("your overweight")
else:
     print("obese")