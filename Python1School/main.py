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

#2a Nu är det dags att köpa vinterkläder. Du ser en fin jacka som kostar 2000 kronor.
# Jackan är på rea, 50%. Skriv ett program som räknar ut hur mycket du behöver betala
# Tips: räkna ut rabatten med formeln: slut_pris = pris * rea_procent / 100.
jackaPris =2000
inputrea= input("Ange en siffra som procent för rean:")
reaProcent= int(inputrea)
#jackaMedRea = int(jackaPris*reaProcent/100)
jackaMedRea = jackaPris * (1 - reaProcent / 100)
print(f"En jacka som kostar {jackaPris}, med {reaProcent}% rea kostar {round(jackaMedRea)}")
#2b Gör om programmet så att användaren kan skriva in en procentsats.
# Här har jag gjort så att man får input i %. Priset gångras med reaprocenten och visas avrundat!





