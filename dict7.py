dict={'x':100,'y':200,'z':400}
key_max=max(dict.key(),key=(lambda k: dict[k]))
key_min=min(dict.key(),key=(lambda k:dict[k]))
print(key_max)
print(key_min)
