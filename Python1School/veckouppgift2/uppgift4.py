#  Temperaturomvandling
# Skriv ett program som kan omvandla en temperatur i grader Celsius till grader Fahrenheit.
cel_grad = input("Skriv in en temperatur i grader Celsius: ")# 22
far_grad = float(cel_grad)*9/5+32
print(f"{cel_grad} grader celsius blir {round(far_grad)} grader fahrenheit ")

# Som function nedan:
# def cel_to_far(cel):
    # return (celsius * 9/5) + 32

# Version 2: fråga först användaren om man vill ange temperaturen i Celsius eller Fahrenheit.
temp_typ = input("Vill du ange temperaturen i Celsius eller Fahrenheit? (Ange C eller F): ")
if temp_typ.upper() == 'C':
    val_c = float(input("Skriv in en temperatur i grader Celsius: "))
    val_f = val_c * 9/5 + 32
    print(f"\n{(val_c)} grader Celsius blir {(val_f)} grader Fahrenheit")
elif temp_typ.upper() == 'F':
    val_f = float(input("Skriv in en temperatur i grader Fahrenheit: "))
    val_c = (val_f - 32) * 5/9
    print(f"\n{(val_f)} grader Fahrenheit blir {(val_c)} grader Celsius")
else:
    print("Ogiltigt val. Var god ange 'C' för Celsius eller 'F' för Fahrenheit.")

# Version 3: om temperaturen som omvandlas är under 10°C ska programmet dessutom säga till användaren att ta
    # på sig vinterkläder. Och om temperaturen är minst 20°C ska det föreslå att man packar badkläder.
if val_c < 10 or val_f < 50:
    print("\nKallt! Ta på dig vinterkläder!")
elif val_c > 20 or val_f > 68:
    print("\nVarmt! Glöm inte packa badkläder")
