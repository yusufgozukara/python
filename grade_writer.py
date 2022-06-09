degree = int(input("Please enter your degree:"))

if degree > 90 :
  if degree > 95 : 
    print("Your degree is A+")
  else:
      print("Your degree is A")
elif degree > 80 :
  if degree > 85 :
    print("Your degree is B+")
  else:
      print("Your degree is B")
else :
  print("Your degree is B-")