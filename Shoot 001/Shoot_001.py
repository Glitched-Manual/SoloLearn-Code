#function for firing ray 

import random

#shots_fired
#
print("Enter a number")


x = int(input()) % 100

chance = (random.randint(0,100) + 1)
#Pass hit ratio and random damage run damage function if hit
def draw(x):

 if chance > x:
   print("\n\nBut, it missed...")
   
 else:
     
   print("Deals Damage")
       
   
draw(x)