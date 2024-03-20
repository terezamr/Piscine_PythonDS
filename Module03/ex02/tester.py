from DiamondTrap import King

Joffrey = King("Joffrey")
print("1: ",Joffrey.__dict__)
Joffrey.set_eyes("blue")
Joffrey.set_hairs("light")
print(Joffrey.get_eyes())
print(Joffrey.get_hairs())
print("2: ",Joffrey.__dict__)