import numpy as np
x=np.array(['python','php','java'],dtype=np.str)
print(x)
new_array=np.char.multiply(x,3)
print(new_array)
