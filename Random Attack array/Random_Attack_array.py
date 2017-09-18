import random

#list of weapons
#weapon names triger dictionaries for attacks

arms = ["lazer_gun","deth_ray","null_ray"]

arms_attack = {"lazer_gun":random.randint(20,40),"deth_ray":random.randint(30,55),
               "null_ray":random.randint(60,90)}


print(arms_attack[arms[0]])

#buffer output
input()