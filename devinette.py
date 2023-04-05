"""Correction de la question "devinette" de la semestrielle.

fait en classe le 11.01.2023"""

import random

BUT = "Votre but est de deviner un nombre entre 1 et 100 que je viens de choisir."
DEVINE = "Quel est mon nombre? "
FAUX = "Ce nombre est trop {}!"
TROUVE = "Bravo! Tu as trouvé en {} essais."

nombre_a_deviner = random.randrange(100) + 1
n_essais = 0
print(BUT)
while True:
    tentative = int(input(DEVINE))
    n_essais += 1
    if tentative == nombre_a_deviner:
        break
    elif tentative < nombre_a_deviner:
        print(FAUX.format("petit"))
    else:
        print(FAUX.format("grand"))
print(TROUVE.format(n_essais))