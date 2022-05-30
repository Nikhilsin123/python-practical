import numpy as np
x=np.array(['python','php','java'],dtype=np.str)
print(x)
stripped=np.char.strip(x)
print("\n remove the leading and trailing whitespaces:",stripped)
