# 1. Vad är syftet med koden?
    # Syftet är att en användare anger en köpsumma som sedan omvandlas
    # till float och jämförs med villkor, för att sedan få en uträknad rabattprocent.

# 2. Testkör koden med några olika värden.
is_member = False
level1 = 100
level2 = 200
discount = 0

price = input("Välkommen, köp något dyrt: ")
price = float(price)
if price > level1:
    print("Grattis! Du har avancerat till nivå 1 och får 10% rabatt")
    discount = discount + 10
if price >= level2:
    print("Grattis! Du har avancerat till nivå 2 och får 25% rabatt")
    discount = discount + 25

final_price = price * (100 - discount)/100
print("Efter rabatter blir priset..." +  str(final_price))

# 3. Finns det några direkta fel i koden? (fel som gör att programmet kraschar)
    #  print("Efter rabatter blir priset..." +  final_price)
    # TypeError: can only concatenate str (not "float") to str

    # Jag konverterade sista printraden med str() så att programmet funkar

# 4. Finns det logiska fel? (programmet gör något annat än det är tänkt)

    # Programmet gör att man kan få ackumulerad rabattprocen, till 35%, istället för en satt på antingen 10% ELLER 25%
    # Rabatten kanske ska avrundas också för att det ska bli snyggare, med round()

# 5. Diskutera möjliga lösningar på felen ni hittat.

    # För att lösa så att man får en icke-ackumulerad rabattprocent, så kan man ändra den andra if-satsen till en elif
    # För att lösa så att man får en avrundad final_price så kan man avrunda variabeln; str(round(final_price)))

# 6. Diskutera möjliga förbättringar på koden
    # Det jag skrev ovan