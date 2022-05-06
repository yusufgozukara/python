for x in numbers:
  frequent = numbers.count(x)
  if(frequent > counter):
    counter = frequent
    value = x
print("The most frequent number is {} and it was {} times repeated".format(value, counter))