# 6 Todo list (att göra-lista) # Bygg ett program där användaren kan lägga till saker till en todo-lista.
# Tips: använd en loop, input och en variabel för listan.
# Exempel:
# ** Todo list extravaganza **
minlista = []
while True:
    print("\nVälj alternativ med siffror.")
    print("1. Se listan")
    print("2. Lägg till punkter i listan")
    print("3. Radera från listan")
    print("Välj alternativ med siffror.")
    svar = input("Svar:")
    svar = int(svar)
    if svar == 1:
        if len(minlista)==0:
            print("listan är tom")
        else:
            print(minlista)
    elif svar ==2:
        print("Vad ska du lägga in för aktitet:")
        nytt = input("Skriv här:")
        minlista.append(nytt)
    elif svar==3:
        print("Vad ska du radera för aktitet:")
        radera = input("Skriv den här:")
        minlista.remove(radera)
