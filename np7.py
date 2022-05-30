import numpy as np
x=np.array(['python','java','php'],dtype=np.str)
print(x)
rstripped_char=np.char.rstrip(x)
print("\n removing the trailing whitespaces:",rstripped_char)
