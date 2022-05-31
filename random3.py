import secrets
secrets generator=secrets.systemRandom()
print("generating 6 digit otp")
otp=secretsgenerator.randrange(100000,999999)
print("secure random otp is",otp)
