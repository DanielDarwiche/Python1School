# test av Loopar:

# Basic While
# siffra = int(input("Skriv en siffra:"))
# while siffra > 0:
#     print(siffra)
#     siffra = siffra - 1
#     print("Inuti loopen")
# print("Loop finished")
# print(f"\n\n{siffra} i slutet")

# While med if sats i
# siffra =int(input("Skriv en siffra:"))
# while siffra != 22:
#     print(f"Siffran {siffra} är inte 22 än")
#     if siffra>22:
#         siffra=siffra-1
#     else:
#         siffra=siffra+1
# print(f"\n\nSiffran är äntligen {siffra}")

# Basic For loop with range
# for i in range(5,15,3):
#     print(str(i))

# Basic For loop with range
# for i in range(3,6,1):
#     print(str(i))

# Basic list
# mi_lista = ["One", 2, "Tres","",5]
# for x in range(3):
#     print(mi_lista[x]) #Skriver värde efter listans index
#
# print(len(mi_lista)) #len = lenght
# mi_lista.append("sista")
# mi_lista[3]=4
# print(mi_lista)
#
# mi_lista.remove(4)
# mi_lista.remove(mi_lista[3]) #index 3 för värde 5
# print("\n\n Utan 4 och 5: " + str(mi_lista))

# List funktioner
# the_list=[1,2,3,4,5,8,7,6,9,10]
# print(the_list.index(1)) #värde 1 har index 0
# print(the_list.count(4)) # 1 förekomst av värde 4
# the_list.sort()
# print(str(the_list) + " Nu har vi sorterat \n")
# the_list.reverse()
# print(str(the_list) + " Nu har vi reversat \n")
# the_list.insert(11,"yo_inserted_here")
# print("the list in the end: " + str(the_list))


# Slice notation -  [start:stop:step] [::]
# num = [1,2,3,4,5]
# print(num[::-1])
# x = "slicing"
# print(x[::]) #inget händer
# print(x[::-1]) #skriver ut backlänges
# print(x[0:2:1]) #index 0,1 = s,l
# print(x[4:6]) #index 4 till 5 in
# print(x[2:]) #start från index 2

# String functions
# ensträng = "index R är 7"
# print(ensträng.find("R")) #index 6
# print(ensträng.find("r")) # index 9
# print(ensträng.find("7")) # index 11
#
# liten = ensträng.lower()
# stor = ensträng.upper()
# liten=liten +". \t samt stor: "+ stor
# print(liten)
#
#
# my_list = ['Detta', 'är', 'en', 'mening']
# result = ' '.join(my_list)
# print(result)  # Utskrift: "Detta är en mening"
#
#
#







