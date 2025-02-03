def average_words(strings):
    found = []
    for item in strings:
        if 4 < len(item) < 8:  #flera villkor i en rad utan or eller and. coolt!
            found.append(item)
    return found
print(average_words(["sup", "how's", "it", "going", "reflecting", "on",
"programs", "and", "coding"]))

def find_min(numbers):
    counter = 0
    for item in numbers:
        if item <counter:
            counter = item
    print(f"The smallest item is {counter}")

find_min([10,3,-11])


# KALLADE FUNKTIONER FRÅN MODULER
import moduler_to_call
moduler_to_call.pro_name("Anders")

moduler_to_call.echoecho("Hallå?")

moduler_to_call.echo("eko..", 6)




end = 5
y = 1
for x in range(1,100):
    y *= 2
    if x == 5:
        break
print(y)




 # Skriv en funktion med namnet last. Den ska ta en
# lista som parameter och returnera det
# sista elementet i listan.
# last([1, 2, 3]) → 3
exempel_lista = [1,7,3,2355]
def last_one(the_list):
    sista = len(the_list)-1 #Längd av lista-1 för indexplats 0 räknas
    return the_list[sista]
# print(last_one(exempel_lista))


def last_one_v2(the_list):
    return the_list[-1]  #Last element in lists
# print(last_one_v2(exempel_lista))


en_lista = ["Bröd", "banan", "äpple", "vindruvor", "kebab"]
def cut_edged(en_lista):
    return list(filter(lambda x:x != en_lista[0] and x != en_lista[-1],en_lista))

print(cut_edged(en_lista))

def incr(x):
    x+=1
    return x
print(incr(1))

def average(x:int, y:int):
    return (x+y)/2

print(round(average(7,5)))

tom_lista = []
exempel_lista = ["Bröd", "Tacos", "Pizza", "Donuts"]
print(exempel_lista)
def pretty_print(lista): #Testa med tom_lista om du vill
    if len(lista) == 0:
        print("Listan är tom!")
    else:
        print(f"\nListan har {len(lista)} element!")
        for i in range(len(lista)):
            print(f"Listans index {[i]} är: {lista[i]}")

pretty_print(exempel_lista)

# FLER UPPGIFTER STÅR PÅ moduler_to_call
