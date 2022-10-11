import mysql.connector
import random

ilma_alukset = ["lentokone", "vesitaso", "helikopteri"]

print("syötä K jos haluat pelata peliä")
print("syötä E jos et halua pelata peliä")
user_answer = input("Syötä K tai E: ").upper()
if user_answer == "K":
    print("Tervetuloa lentopeliin")
    print("Valitse ilma-alus:")
    print(f"Lista ilma-aluksista: {ilma_alukset}")
    ilma_alus_input = ""
    while ilma_alus_input != "lentokone" or "vesitaso" or "helikopteri":
        ilma_alus_input = input("Syötä ilma-alus: ").lower()
        if ilma_alus_input == "lentokone":
            print("valitsit cesna 172 lentokoneen")
            print("cesna 172 on lentokone, jolla voi lentää kerralla maksimissaan 1185 km pitkän matkan")
            break
        elif ilma_alus_input == "vesitaso":
            print("valitsit cesna 185 vesitason")
            print("cesna 185 on vesitaso, jolla voi lentää kerralla maksimissaan 933 km pitkän matkan")
            break
        elif ilma_alus_input == "helikopteri":
            print("valitsit airbus H135 helikopterin")
            print("airbus H135 on helikopteri, jolla voi lentää kerralla maksimissaan 633 km pitkän matkan")
            break
        else:
            print("Virheellinen ilma-alus")
            print("Syötä ilma-alus uudelleen")

    yhteys = mysql.connector.connect(
        host='127.0.0.1',
        port=3306,
        database='flight_game',
        user='benjamn',
        password='Metrolippu23',
        autocommit=True
    )

    suomen_lentokentät = []
    sql = "SELECT name FROM airport WHERE iso_country = 'FI'"
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    """for rivi in tulos:
        print(f"{rivi[0]}")"""

    maailman_lentokentät = []
    sql2 = "SELECT name FROM airport"
    kursori1 = yhteys.cursor()
    kursori1.execute(sql2)
    tulos2 = kursori1.fetchall()
    maailman_lentokentät.append(tulos2)

    valittu_kenttä = random.choice(tulos)
    # print(valittu_kenttä)

    print(f"{ilma_alus_input} lähtee kohteesta {valittu_kenttä} ")

    if ilma_alus_input == "lentokone":d
wdawd










elif user_answer == "E":
    print("Lopetit pelin!")
    print("Haluatko antaa palautetta? ")
    print("Syötä K jos haluat antaa palautetta tai syötä E jos et halua antaa palautetta.")
    user_help_answer = input("Haluatko antaa palautetta (K / E)? ").upper()
    if user_help_answer == "K":
        input("Anna palautetta: ")
        print("Kiitos palautteesta!")
    elif user_help_answer == "E":
        print("Peli ohi")








#Github testi lololololololoooooooooo