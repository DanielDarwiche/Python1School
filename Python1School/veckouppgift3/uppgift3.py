# 3 Kvittouträknaren
# Gör ett program som upprepade gånger ber användaren skriva in ett tal. När man skriver in strängen
# "quit" eller "avsluta" ska programmet ska det räkna ut summan av talen.
# Exempel:.....# Välkommen till Kvittokompis! Avsluta genom att skriva: quit
# Skriv in ett belopp: 25...# Skriv in ett belopp: 50.....# Skriv in ett belopp: quit...# Det blir 75 kr totalt. Välkommen åter!
# summa=0
# print("Välkommen till kvittouträknaren. Avsluta genom att skriva 'avsluta'")
# while True:
#     svar = input("Skriv in ett belopp: ")
#     if str(svar).lower() == "avsluta":
#         break
#     else:
#         svar = int(svar)
#         summa+=svar
# print(f"Det blir {summa} totalt. Välkommen åter")

# Med try except
# summa=0
# print("Välkommen till kvittouträknaren. Avsluta genom att skriva 'avsluta'")
# while True:
#     svar = input("Skriv in ett belopp: ")
#     if str(svar).lower() == "avsluta":
#         break
#     try:
#         svar = int(svar)
#         summa+=int(svar)
#     except:
#         print("Nu blev det fel. Ange en summa eller skriv 'avsluta'")
# print(f"Det blir {summa} totalt. Välkommen åter")

# Version 2: programmet ska fråga hur många man är, och tala om hur mycket varje person i sällskapet ska betala.

summa=0
antal = input("Välkommen till kvittouträknaren. \nAvsluta genom att skriva 'avsluta'\nSkriv in hur många ni är: ")
if antal.isdigit()==False:
    raise TypeError("Det är fel typ, du måste skriva siffror")
# if not type(int(antal)) is int:           #Samma som ovan
#     raise TypeError("Only integers are allowed")

if int(antal) < 1:
    raise Exception("Du kan vara minst en person")

while True:
    svar = input("Skriv in ett belopp: ")
    if str(svar).lower() == "avsluta":
        break
    else:
        svar = int(svar)
        summa+=svar
belopp = float(summa)/float(antal)
print(f"Det blir {belopp} totalt. Välkommen åter")



































































# Hur många är ni? 3......  Det blir 75 kr totalt, alltså 25.0 kr per person. Välkommen åter!

# try except med else och finally
# try:
#     # f = open("demofile.txt") #This will go wrong
# 	print(2)    #this will not go wrong
# except:
#     print("Something went wrong")
# else:
#     # f.write("Lorum Ipsum")#This will go wrong
# 	print(3)    #this will not go wrong
# finally:
#     print("Always writes this")
