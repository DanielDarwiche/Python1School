import random
from turtledemo.penrose import start


def pro_name(name):
    print(f"{name} is a real hacker pro!")

def echoecho(echo):
    print(echo + ".." + echo + ".." + echo)

def echo(echo, antal:int):
    ekot= ""
    for i in range(antal):
        ekot+= str(echo)
    print(ekot)



# Spelet 21
def first_sum_over_21():
    start = 1
    while True:
        if start <= 21:
            start+=1
            print(start)
        else:
            False
    return start

# print(first_sum_over_21())

# v2

def first_sum():
    start = 0
    while True:
        if start <= 21:
            start+= random.randint(1,13)
            print("Draget kort: "+str(start))
        else:
            False
    return start

print(first_sum())
