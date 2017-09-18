import random

#list of weapons
#weapon names triger dictionaries for attacks

arms = ["lazer_gun","deth_ray","null_ray"]

arms_attack = {"lazer_gun":random.randint(20,40),"deth_ray":random.randint(30,55),
               "null_ray":random.randint(60,90)}

user_input = int(input()) % 3

print("You selected the "+ str(arms[user_input]) + " you deal " + str(arms_attack[arms[user_input]]) + " to the target!\n")

#buffer output
