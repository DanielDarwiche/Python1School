# 1a Skriv färdigt kodexemplet....Svaret ska bli 55
# answer = 0
# for i in range(11):
#     answer += i
# print("Summan av talen 1 till 10 är: " + str(answer))

# 1b Räkna ut summan av alla tal mellan 1 och 100.
# inkl 1 & 100, rätt svar ska bli 5050.
# answer = 0
# for i in range(101):
#     answer += i
# print("Summan av talen 1 till 10 är: " + str(answer))

# 1c Skriv om 1b så att den använder en while-loop.
# answer = 0
# while answer!=5050:
#     for i in range(101):
#         answer += i
# print("Summan av talen 1 till 10 är: " + str(answer))

# 2 Räkna ut summan av alla elementen i listan: [1, -2, 3, -2, 4, -3]
# lista= [1, -2, 3, -2, 4, -3]
# sum = 0
# for r in range(len(lista)):
#     sum+= lista[r]
# print(str(sum))


# 3 Träna på att skapa och manipulera listor. Alla uppgifter ska lösas med funktionerna som
# står i presentationen.
# 3a Skapa en lista med namnen på fyra filmer. Namnen ska vara strängar. Skriv ut hela listan
# 2med funktionen print.
my_films = ["Atlatic", "Titanic", "The hobbit", "Lord of the rings"]
print(my_films)
# 3b Lägg till "Fellowship of the ring" sist i listan.
my_films.append("Fellowship of the ring")
print(my_films) #Skriver ut listan inkl det nya värdet
# 3c Lägg till "The two towers" på första platsen i listan. (index noll)
my_films.insert(0,"The two towers")
print(my_films) #Skriver ut listan inkl det nya värdet
# 3d Ta reda på vilken position (index) "Fellowship of the ring" har nu.
indexvärde = my_films.index("Fellowship of the ring")
print(f"Filmen är på index {indexvärde}")
# 3e Ta bort en annan av filmerna. Har Fellowship-filmen ändrat index?
my_films.remove("Titanic")
indexvärde = my_films.index("Fellowship of the ring")
print(f"Filmen är på index {indexvärde}")   #Indexvärdet är inte detsamma nu
# 3f Ta reda på hur lång listan är. (len)
print("Listans längd är " + str(len(my_films)))
# 3g Vänd listan baklänges.
my_films.reverse()
# 3h Sortera listan stigande i bokstavsordnin
my_films.sort()
print(my_films)