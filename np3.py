import numpy as np
x=np.array(['python','php','java']
print(x)
encoded_char=np.char.encoded(x,'cp500')
decoded_char=np.char.decode(encoded_char,'cp500')
print(encoded_char)
print(decoded_char)
