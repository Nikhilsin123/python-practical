import numpy as np
x=np.array(["python","php"],dtype=np.str)
y=np.array(["java","c++"],dtype=np.str)
print(x)
print(y)
new_array=np.char.add(x,y)
print(new_array)
