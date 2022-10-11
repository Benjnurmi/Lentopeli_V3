import mysql.connector
import random
import geopy.distance


"""random = ["dd", "ggg", "lll"]
print(f"syötä mihin kenttään haluat lentää {random}")
käyttäjä = input("syötä numero 1-3")
if käyttäjä == "1":
    print(random[0])
elif käyttäjä == "2":
    print(random[1])
elif käyttäjä == "3":
    print(random[2])"""


ilma_alukset = ["lentokone", "vesitaso", "helikopteri"]  # lista, jossa on pelissä käytettävät ilma-alukset


print("syötä K jos haluat pelata peliä")
print("syötä E jos et halua pelata peliä")
user_answer = input("Syötä K tai E: ").upper()  # Haluaako pelata vai ei?
if user_answer == "K":
    print("Tervetuloa lentopeliin")
    print("Valitse ilma-alus:")
    print(f"Lista ilma-aluksista: {ilma_alukset}")  # lista ilma-aluksista
    ilma_alus_input = ""
    while ilma_alus_input != "lentokone" or "vesitaso" or "helikopteri":
        ilma_alus_input = input("Syötä ilma-alus: ").lower()  # ilma-aluksen valinta
        if ilma_alus_input == "lentokone":  # jos pelaaja  valitsee lentokoneen
            print("valitsit cesna 172 lentokoneen")
            print("cesna 172 on lentokone, jolla voi lentää kerralla maksimissaan 1185 km pitkän matkan")
            break
        elif ilma_alus_input == "vesitaso":  # jos pelaaja valitsee vesitason
            print("valitsit cesna 185 vesitason")
            print("cesna 185 on vesitaso, jolla voi lentää kerralla maksimissaan 933 km pitkän matkan")
            break
        elif ilma_alus_input == "helikopteri":  # jos pelaaja valitsee helikopterin
            print("valitsit airbus H135 helikopterin")
            print("airbus H135 on helikopteri, jolla voi lentää kerralla maksimissaan 633 km pitkän matkan")
            break
        else:
            print("Virheellinen ilma-alus")  # jos pelaaja syöttää virheellisen ilma-aluksen
            print("Syötä ilma-alus uudelleen")


    yhteys = mysql.connector.connect(   #  sql yhteys
        host='127.0.0.1',
        port=3306,
        database='flight_game',
        user='tomih',
        password='salasana123',
        autocommit=True
    )

    suomen_lentokentät = []  # lista suomessa sijaitsevista lentokentistä
    sql1 = "SELECT name, latitude_deg, longitude_deg FROM airport WHERE iso_country = 'FI'"
    kursori = yhteys.cursor()
    kursori.execute(sql1)
    tulos1 = kursori.fetchall()
    """for rivi in tulos1:
        print(f"{rivi[0]}")"""

    valittu_kenttä = random.choice(tulos1)
    # print(valittu_kenttä)

    print(f"{ilma_alus_input} lähtee kohteesta {valittu_kenttä[0:3]} ")


    maailman_lentokentät = []
    sql2 = "SELECT name, latitude_deg, longitude_deg FROM airport"
    kursori1 = yhteys.cursor()
    kursori1.execute(sql2)
    tulos2 = kursori1.fetchall()

    # print(maailman_lentokentät)
    for n  in range (5):
        random_kentät = random.choice(tulos2)
        maailman_lentokentät.append(random_kentät)
        # print(random_kentät)


    #  me_consumed = '0';T co2
    # UPDATE ga  SE

    def co2_usage():
        co2_lista = []
        sql3 = "SELECT co2_consumed, co2_budget FROM game"
        kursori2 = yhteys.cursor()
        kursori2.execute(sql3)
        tulos3 = kursori2.fetchall()
        for rivi in tulos3:
            print(f"{rivi[0]}")



    print("Valitse seuraavasta listasta mihin haluat lentää! ")
    print(maailman_lentokentät)
    matka1_input = input("Syötä numero (1-5):  ")
    if matka1_input == "1":
        print(f"Valitsit matkan kohteeksi {maailman_lentokentät[0]}")
    elif matka1_input == "2":
        print(f"Valitsit matkan kohteeksi {maailman_lentokentät[1]}")
    elif matka1_input == "3":
        print(f"Valitsit matkan kohteeksi {maailman_lentokentät[2]}")
    elif matka1_input == "4":
        print(f"Valitsit matkan kohteeksi {maailman_lentokentät[3]}")
    elif matka1_input == "5":
        print(f"Valitsit matkan kohteeksi {maailman_lentokentät[4]}")

    print(f"Lähtökentän sijainti on {valittu_kenttä[1:3]}")
    print(f"Matkan kohteen sijainti ")





















    """if ilma_alus_input == "lentokone":"""












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










#Tomin koodit ylhäällä