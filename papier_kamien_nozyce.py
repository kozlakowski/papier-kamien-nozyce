#                          ZASADY GRY

# kamień = 1
# papier = 2
# nożyce = 3

import random

punkty = 0


def zamiana_programu():
    global wybor_programu

    if wybor_programu == 1:
        wybor_programu = "kamien"

    elif wybor_programu == 2:
        wybor_programu = "papier"

    elif wybor_programu == 3:
        wybor_programu = "nozyce"





while punkty <= 5:

    wybor_gracza = input("Wpisz czy wybierasz kamien, papier, nozyce : ")
    wybor_gracza = wybor_gracza.lower()

    wybor_programu = random.randrange(1,4)
    zamiana_programu()

    print("Wybór gracza to :", wybor_gracza)
    print("Wybór programu to :", wybor_programu)


    if wybor_gracza == wybor_programu:
        pass

    elif (wybor_gracza == "kamien") and (wybor_programu == "nozyce"):
        punkty += 1

    elif (wybor_gracza == "papier") and (wybor_programu == "kamien"):
        punkty += 1

    elif (wybor_gracza == "nozyce") and (wybor_programu == "papier"):
        punkty += 1

    else:
        print("Przegrałeś")


    print("Aktualna liczba punktów to :", punkty)



