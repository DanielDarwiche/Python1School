# Miniräknare
# 1 Gör ett program som frågar användaren efter 3 tal. Sedan ska det räkna ut vad summan
# blir, och skriva ut på konsolen. (summa: tal1 + tal2 + tal3)
tal_ett = input("Skriv in tal 1: ")
tal_två = input("Skriv in tal 2: ")
tal_tre = input("Skriv in tal 3: ")
print("Nu ska du få se!\nTalen blir tillsammans: " + str(float(tal_ett)+float(tal_två) + float(tal_tre)))
# 2 Programmet ska tala om vilket som är det största talet, utan att använda Python-funktionen max.
# Använd i stället if/elif/else.
största_talet = 0
if tal_ett >= tal_två and tal_ett >= tal_tre:
    största_talet = tal_ett
elif tal_två >= tal_tre and tal_två >= tal_ett:
    största_talet = tal_två
elif tal_tre >= tal_två and tal_tre >= tal_ett:
    största_talet = tal_tre

# 3 Programmet ska tala om ifall två av talen är lika, eller alla tre är lika.
if tal_ett == tal_två and tal_ett == tal_tre and tal_två == tal_tre:
    print("Talen är lika stora")
else:
    print("Det största talet är:", största_talet)
