# Balder

print("Välkommen till Balder!")
length = input("Hur lång är du? Ange i cm:")
length=int(length)
if length>= 130:
    print("Jippi! Du får åka!")
else:
    print("Tyvärr! Du får inte åka!")

# Varför ange dessa värden?(121, 130, 155)
# För att varje värde ger olika logiska utfall.
# Testvärdet 129 är mindre än 130 och bör inte tillåta att åka.
# Med andra ord är värdet 129, rent logiskt, inte nödvändigt, men kan vara intressant som manuellt test.





