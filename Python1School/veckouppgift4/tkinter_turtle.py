#                           tkinter!
# import tkinter as tk
#
# root = tk.Tk()
# root.title("Tkinter Test")
# label = tk.Label(root, text="Hello, Tkinter!")
# label.pack()
# root.mainloop()



import turtle as t

# Upprepa 3 gånger

# for x in range(3):
#     t.forward(100)
#     t.left(120)
#     t.penup()   # Lyft pennan för att flytta utan att rita
#     t.forward(200)
#     t.pendown()
#     t.dot(10, "red")
#     t.color("blue")
#     t.forward(50)
#     t.mainloop()    # Låt fönstret stanna kvar tills användaren stänger det


def draw_square(side_length):
    for _ in range(4):
        t.forward(side_length)
        t.right(90)

t.speed(1)  # 1 är långsammast, 10 är snabbast
# draw_square(100)  # Ritar en kvadrat med sidlängd 100
t.done()  # Håller fönstret öppet


# # 2 Skriv en funktion som flyttar pennan ett lämpligt avstånd till höger, utan att rita.
# # Tanken är att du ska kunna kombinera den med kvadratfunktionen, för att rita flera kvadrater.
# def draw_square(side_length):
#     for _ in range(4):
#         t.forward(side_length)
#         t.right(90)
# def move_next(distance):
#     t.penup()
#     t.forward(distance)
#     t.pendown()
# screen = t.Screen()
# t.speed(1)
# for x in range(5):
#     draw_square(100)
#     move_next(90)
# t.done()


# # 3 Bygg om koden så att den ingår i en funktion, som ritar en komplett cirkel. Använd parametrar i stället för värdena 7, 40 och 30.
# # Tips 1: vad händer om man varierar värdet på range?         # Tips 2: 360 grader motsvarar ett helt varv.
# for x in range(7):
#     t.forward(40)
#     t.right(30)


# # 4 Skriv funktioner som ritar de enskilda bokstäverna i ordet "PYTHON" med turtle-modulen.
# # Kombinera dem och försök få bokstäverna att ritas med samma storlek, på en rak linje.


