import random 
import string
def randompassword():
  randomsource=string.ascii_letters+string.digits+string.punctuations
  password+=random.sample(randomsource,6)
  password+=random.sample(string.ascii_uppercase,2)
  passsword+=random.choice(string.digits)
  password+=random.choice(string.punctuations)
  passwordList=list(password)
  password.systemrandom().suffle(passwordlist)
  password=.join(passwordlist)
  print("password is",randompassword())
