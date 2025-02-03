from veckouppgift4 import matte_module
from veckouppgift4.matte_module import print_all_modules, add, minus
from veckouppgift4.matte_module import times as gångerfunktionen

def min_funktion():
    print("Test av funktion\nBör skriva text i konsoll")

min_funktion()

def para_fun(animal, feeling):
    print(f"\nThe {animal} is feeling {feeling}")

para_fun("cat", "Happy")
para_fun("Dog", "Sleepy")
para_fun("Lion", "Hungry")

# alternativ parametrar för funktionen!
para_fun(feeling="Supersad", animal="Giant bunny")



# funktion med returvärde och spara det
totalsumman=0
def add(tal1,tal2):
    return tal1+tal2

print(f"Totalsumman är {totalsumman} nu")
totalsumman = add(3,5)

print(f"Totalsumman är {totalsumman} nu")
totalsumman += add(100,100)
print(f"Totalsumman är {totalsumman} nu")

add(1000,15000) #Utan print => osynlig

# LAMBDA-funktioner
times_ten = lambda n:n * 10

ten_m_print = lambda \
        n:n * 10    #;print("anonym lambda med print användes")
# print(ten_m_print)

def lamdafunken(n):
    print("lamdafunken användes!")
    return n*10.75

print(f"Skriver ut times_ten {times_ten(1)}")
print(f"Skriver ut lamdafunken {lamdafunken(1)}")


# Lambda
litenlista = [1,2,3,4,5,6,7,8]
jämnlista = list(filter(lambda x:x %2==0, litenlista))
print (jämnlista)

en_mening= "Detta är otydligt en obrukbar o-lista med totalt 5 o"
antal_o = list(filter(lambda x:x == "o", en_mening))
print(f"Antal o: {len(antal_o)}. Hela listan: {antal_o}")

# Filter med lambda
antal_av_k=0
en_mening= "Detta är ktydligt en kbruobar k-lista med tktalt 5 k"
hämtade_k = len(list(filter(lambda x:x == "k", en_mening)))
antal_av_k += hämtade_k
print(f"Antal av k: {antal_av_k} ")
# print(f"Antal o: {len(antal_o)}. Hela listan: {antal_o}")


stor_lista = [6,7,8,9,10]
even_2 = []
for siffra in stor_lista:
    if siffra % 2 == 0: #Jämna tal
        even_2.append(siffra) #Lägg i den nya listan

print(even_2)

# en till for loop
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# map
old_fruit = ["pera", "manzana", "Platano"]
new_models = list(map(lambda z:z + "2", old_fruit))
print(new_models)

# logisk map
prices = [20, 100, 150, 180]
# with_discount = list(map(lambda x:x*0.9, prices)) #float
# with_discount = list(map(lambda x: int(x*0.9), prices)) #int
with_discount = list(map(lambda x: round(x*0.9), prices)) #avrundat. round(x*0.9,1) = 1 decimal
print(f"Prices: {prices} and with 10% discount: {with_discount}")

expe_prices= []
for i in range(len(prices)):
    expe_prices.append(prices[i]+50)
print(f"Prices: {prices} are now: {expe_prices}")


# importerar short_math_module näst högst upp!
print_all_modules()
print("Då testar vi dem också!")
print(add(10,5))
print(minus(100,5))
# importerad med annat funktionsnamn
print(gångerfunktionen(5,5))

# denna importeras här i koden högst upp
matte_module.jello()



# def is_number(x):
#     if isinstance(x, int):
#         return True
#     elif isinstance(x, bool):
#         return True
#     return False
# print(is_number(5.5))