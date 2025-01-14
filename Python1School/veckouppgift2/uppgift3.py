# Sportresultat
tottenham = "Tottenham"
liverpool = "Liverpool"
tottenham_goals=0
liverpool_goals=0

tottenham_goals=input("Hur många mål gjorde {}? ".format("Tottenham"))
liverpool_goals=input("Hur många mål gjorde {}? ".format("Liverpool"))
tottenham_goals=int(tottenham_goals)
liverpool_goals=int(liverpool_goals)

if tottenham_goals > liverpool_goals:
    print("Tottenham gjorde fler mål, och vann!")
elif tottenham_goals==liverpool_goals:
    print("Eftersom det blev lika många mål, blev det LIKA!")
else:
    print("Liverpool gjorde fler mål, och vann!")

if tottenham_goals > liverpool_goals:
    print("Tottenham hade {} fler mål".format(tottenham_goals-liverpool_goals))
elif tottenham_goals<liverpool_goals:
    print("Liverpool hade {} fler mål".format(liverpool_goals-tottenham_goals))
