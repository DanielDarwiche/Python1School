from datetime import datetime, timedelta
from datetime import date

# 3a Skriv ett program som talar om dagens datum.
print(f"Dagens datum är: {datetime.now()}")
print(f"Det blir lite rörigt.. Såhär då! \n'{date.today()}'")

# 3b (svårare) Ändra programmet så att det kan tala om vilket datum det är om 7 dagar.

framtida_datum = date.today() + timedelta(days=7)
print(f"Datumet om 7 dagar är: {framtida_datum}")
