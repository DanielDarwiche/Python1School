#Uppgift 1
from linecache import clearcache

#1
mittnamn= "Daniel Darwiche"
print("Hello Daniel Darwiche")
print("This program was made by " + mittnamn)

#2
#Vad blir fel?
Price = 100  # biljettpris
Wallet = 200  # pengar på fickan
#print("Det blir " + (y - x) " kronor över.")
#Ovan blir fel för att printfunktionen använder string. Samt att + behövs
calc = Price - Wallet
print("Det blir " + (str(calc)) +"  kronor över.")
# Ovan och neda blir rätt pga string och int differentiering samt rätt strängkonkatenering.
z = (200 - 100) / 2
print("Hälften av resterande 100 är: " , str(z))

# 3
#1a Använd input för att be användaren om ett heltal. Spara värdet i en variabel.
# Omvandla variabelns värde till ett heltal, och skriv ut det för att testa om du har gjort rätt
# Kodexempel med input:x = input("Fråga här")
heltal = input("Ange ett heltal ")
annatTal = input ("Du angav heltalet: " + heltal+". Var god ange ett annat heltal!")
total= int(heltal)+int(annatTal)
print(f"Plussar man {heltal} och {annatTal} blir summan {str(total)} ")
