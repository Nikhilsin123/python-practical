def randomstring(stringLength)
print("generate a random string of 5 characters")
letters=string.ascii_letters
return.join(random.choice(letters)for i in range (stringLength))
print("Random string is",randomString(5))
