def factorial(num)
fact=1
while(num!=0):
  fact*=num
  num=num-1
  print("the factorial is",fact)
  num=int(input("enter a number"))
  factorial(num)
     
