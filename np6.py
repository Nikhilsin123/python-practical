import numpy as np
x=np.array(['python','php','java'],dtype=np.str)
print(x)
lstripped_char=np.char.lstrip(x)
print("\nremove the leading whitespaces:",lstripped_char)
