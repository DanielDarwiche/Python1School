# 5 Gissa talet
# Gör ett spel som slumpar ett hemligt tal mellan 1 och 100. Sedan ska man försöka gissa
# det. Om man gissar för lågt eller för högt ska spelet tala om det. Efter att man har gissat
# rätt ska spelet skriva ut antalet gissningar.
# # Slumpa ett hemligt tal
import random
antalgissningar=0
secret = random.randint(1, 100)
loopen=True
while loopen == True:
    svar = input("Gissa talet! ")
    antalgissningar += 1
    svar=int(svar)
    if int(svar)==int(secret):
        print("\nRätt gissat!")
        loopen=False
    else:
        print("Det var fel, gissa igen!")
        if svar<secret:
            print("Talet är större!")
        elif svar> secret:
            print("Talet är mindre")
print(f"Du gissade {antalgissningar} gånger!")
