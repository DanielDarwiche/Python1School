#2a Nu är det dags att köpa vinterkläder. Du ser en fin jacka som kostar 2000 kronor.
# Jackan är på rea, 50%. Skriv ett program som räknar ut hur mycket du behöver betala
# Tips: räkna ut rabatten med formeln: slut_pris = pris * rea_procent / 100.
jackaPris =2000
inputrea= input("Ange en siffra som procent för rean:")
reaProcent= int(inputrea)
jackaMedRea = jackaPris * (1 - reaProcent / 100)
print(f"En jacka som kostar {jackaPris}, med {reaProcent}% rea kostar {round(jackaMedRea)}")
#2b Gör om programmet så att användaren kan skriva in en procentsats.
# Här har jag gjort så att man får input i %. Priset gångras med reaprocenten och visas avrundat!


