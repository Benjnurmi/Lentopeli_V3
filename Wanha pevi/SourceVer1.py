import mysql.connector
import random
import geopy.distance


ilma_alukset = ["lentokone", "vesitaso", "helikopteri"]  # lista, jossa on pelissä käytettävät ilma-alukset

print("syötä K jos haluat pelata peliä")
print("syötä E jos et halua pelata peliä")
user_answer = input("Syötä K tai E: ").upper()  # Haluaako pelata vai ei?
if user_answer == "K":
    print("Tervetuloa lentopeliin")
    print("Lentopelin idea on lentää ympäri maailmaa ja kerätä pisteitä.")
    print()
    print("Valitse ilma-alus:")
    print(f"Lista ilma-aluksista:")
    print(*ilma_alukset, sep = ', ')
    ilma_alus_input = ""
    while ilma_alus_input != "lentokone" or "vesitaso" or "helikopteri":
        ilma_alus_input = input("Syötä ilma-alus: ").lower() # ilma-aluksen valinta
        print()
        if ilma_alus_input == "lentokone":  # jos pelaaja  valitsee lentokoneen
            print("valitsit cesna 172 lentokoneen")
            break
        elif ilma_alus_input == "vesitaso":  # jos pelaaja valitsee vesitason
            print("valitsit cesna 185 vesitason")
            break
        elif ilma_alus_input == "helikopteri":  # jos pelaaja valitsee helikopterin
            print("valitsit airbus H135 helikopterin")
            break
        else:
            print("Virheellinen ilma-alus")  # jos pelaaja syöttää virheellisen ilma-aluksen
            print("Syötä ilma-alus uudelleen")

    yhteys = mysql.connector.connect(  # sql yhteys
        host='127.0.0.1',
        port=3306,
        database='flight_game',
        user='benjamn',
        password='Metrolippu23',
        autocommit=True
    )


    sql1 = "SELECT name, latitude_deg, longitude_deg FROM airport WHERE iso_country = 'FI'"
    kursori = yhteys.cursor()
    kursori.execute(sql1)
    tulos1 = kursori.fetchall()

    valittu_kenttä = random.choice(tulos1)
    # print(valittu_kenttä)

    print(f"{ilma_alus_input} lähtee kohteesta {valittu_kenttä[0]} ")

    maailman_lentokentät = []
    sql2 = "SELECT name, latitude_deg, longitude_deg FROM airport"
    kursori1 = yhteys.cursor()
    kursori1.execute(sql2)
    tulos2 = kursori1.fetchall()
    matkan_päämäärä = random.choice(tulos2)

    # print(f"Lähtökentän sijainti on {valittu_kenttä[0]}")
    print(f"Matkan kohteen sijainti on {matkan_päämäärä[0]} ")

    coords_1 = (valittu_kenttä[1:3])
    # print(maailman_lentokentät[1:3])
    coords_2 = (maailman_lentokentät[1:3])
    # print(geopy.distance.geodesic(coords_1, coords_2).km)

    matkojen_etäisyys_km = geopy.distance.geodesic(coords_1, coords_2).km
    # print(matkojen_etäisyys_km)

    piste_kaava = matkojen_etäisyys_km * 0.05


    if ilma_alus_input == "lentokone":
        kulutus_kaava1 = matkojen_etäisyys_km * 13

        print(f"{valittu_kenttä[0]} - {matkan_päämäärä[0]} etäisyys on {round(matkojen_etäisyys_km)} km")
        print()
        print("Lennetään...")
        print()
        print(f"{valittu_kenttä[0]} - {matkan_päämäärä[0]} välillä kului bensaa {round(kulutus_kaava1)} litraa ")
        print()
        print(f"Keräsit matkasta pisteitä yhteensä {round(piste_kaava)}")

    elif ilma_alus_input == "vesitaso":
        kulutus_kaava2 = matkojen_etäisyys_km * 20

        print(f"{valittu_kenttä[0]} - {matkan_päämäärä[0]} etäisyys on {round(matkojen_etäisyys_km)} km")
        print()
        print("Lennetään...")
        print()
        print(f"{valittu_kenttä[0]} - {matkan_päämäärä[0]} välillä kului bensaa {round(kulutus_kaava2)} litraa ")
        print()
        print(f"Keräsit matkasta pisteitä yhteensä {round(piste_kaava)}")

    elif ilma_alus_input == "helikopteri":
        kulutus_kaava3 = matkojen_etäisyys_km * 15
        print(f"{valittu_kenttä[0]} - {matkan_päämäärä[0]} etäisyys on {round(matkojen_etäisyys_km)} km")
        print()
        print("Lennetään...")
        print()
        print(f"{valittu_kenttä[0]} - {matkan_päämäärä[0]} välillä kului bensaa {round(kulutus_kaava3)} litraa ")
        print()
        print(f"Keräsit matkasta pisteitä yhteensä {round(piste_kaava)}")

pisteet = []
pisteet.append(piste_kaava)
piste_summa = sum(pisteet)

print()
print("Kirjoita K jos haluat jatkaa lentämistä tai kirjoita L jos haluat lopettaa heti")
user_answer2 = input("Syötä vastaus (K / L) : ").upper()
if user_answer2 == "K":
    matkan_päämäärä2 = random.choice(tulos2)
    print(f"Lähdet matkaan kentältä:{matkan_päämäärä[0]} ja seuraava päämääräsi on {matkan_päämäärä2[0]} ")

    koordinaatit_1 = matkan_päämäärä[1:3]
    koordinaatit_2 = matkan_päämäärä2[1:3]
    matkojen_etäisyys = geopy.distance.geodesic(koordinaatit_1, koordinaatit_2).km

    piste_kaava = matkojen_etäisyys * 0.05
    print(f"{matkan_päämäärä[0]} - {matkan_päämäärä2[0]} etäisyys on {round(matkojen_etäisyys)} km")
    print()
    print("Lennetään...")
    print()
    print(f"{matkan_päämäärä[0]} - {matkan_päämäärä2[0]} välillä kului bensaa {round(piste_kaava)} litraa ")
    print()
    print(f"Keräsit matkasta pisteitä yhteensä {round(piste_kaava)}")

    matkan_päämäärä = matkan_päämäärä2
    pisteet.append(piste_kaava)
    piste_summa = sum(pisteet)












    """print("Lista aluksista: ")
    print(*ilma_alukset, sep=', ')
            ilma_alus_input3 = input("Syötä millä ilma-aluksella haluat lentää? ")
            if ilma_alus_input3 == "lentokone":
                print("Valitsit lentokoneen! ")
            elif ilma_alus_input3 == "vesitaso":
                print("Valitsit vesitason")
            elif ilma_alus_input3 == "helikopteri":
                print("Valitsit helikopterin")
            matkan_päämäärä2 = random.choice(tulos2)
            print(f"Lähdet matkaan kentältä:{matkan_päämäärä[0]} ja seuraava päämääräsi on {matkan_päämäärä2[0]} ")

            koordinaatit_1 = matkan_päämäärä[1:3]
            koordinaatit_2 = matkan_päämäärä2[1:3]
            matkojen_etäisyys = geopy.distance.geodesic(koordinaatit_1, koordinaatit_2).km

            piste_kaava = matkojen_etäisyys * 0.05

            if ilma_alus_input3 == "lentokone":
                kaava1 = matkojen_etäisyys * 13
                print(f"{matkan_päämäärä[0]} - {matkan_päämäärä2[0]} etäisyys on {round(matkojen_etäisyys)} km")
                print()
                print("Lennetään...")
                print()
                print(f"{matkan_päämäärä[0]} - {matkan_päämäärä2[0]} välillä kului bensaa {round(kaava1)} litraa ")
                print()
                print(f"Keräsit matkasta pisteitä yhteensä {round(piste_kaava)}")
            elif ilma_alus_input3 == "vesitaso":
                kaava2 = matkojen_etäisyys * 20
                print(f"{matkan_päämäärä[0]} - {matkan_päämäärä2[0]} etäisyys on {round(matkojen_etäisyys)} km")
                print()
                print("Lennetään...")
                print()
                print(f"{matkan_päämäärä[0]} - {matkan_päämäärä2[0]} välillä kului bensaa {round(kaava2)} litraa ")
                print()
                print(f"Keräsit matkasta pisteitä yhteensä {round(piste_kaava)}")
            elif ilma_alus_input3 == "helikopteri":
                kaava3 = matkojen_etäisyys * 15
                print(f"{matkan_päämäärä[0]} - {matkan_päämäärä2[0]} etäisyys on {round(matkojen_etäisyys)} km")
                print()
                print("Lennetään...")
                print()
                print(f"{matkan_päämäärä[0]} - {matkan_päämäärä2[0]} välillä kului bensaa {round(kaava3)} litraa ")
                print()
                print(f"Keräsit matkasta pisteitä yhteensä {round(piste_kaava)}")


            matkan_päämäärä = matkan_päämäärä2
            pisteet.append(piste_kaava)
            piste_summa = sum(pisteet)


        if user_answer2 == "L":
            print("Kiitos pelaamisesta")
            print(f"Keräsit lentopelin aikana {round(piste_summa)} pistettä!")
            print()
            print("Lopetit pelin!")
            print()
            print("Haluatko antaa palautetta? ")
            print("Syötä K jos haluat antaa palautetta tai syötä E jos et halua antaa palautetta.")
            user_help_answer = input("Haluatko antaa palautetta (K / E)? ").upper()
            if user_help_answer == "K":
                input("Anna palautetta: ")
                print()
                print("Kiitos palautteesta!")
            elif user_help_answer == "E":
                print("Peli ohi!")
                break


        elif user_answer2 == "L":
            print("Kiitos pelaamisesta")
            print("Syötä K jos haluat antaa palautetta tai syötä E jos et halua antaa palautetta.")
            user_help_answer = input("Haluatko antaa palautetta (K / E)? ").upper()
            if user_help_answer == "K":
                input("Anna palautetta: ")
                print()
                print("Kiitos palautteesta!")
            elif user_help_answer == "E":
                print("Peli ohi!")"""


elif user_answer == "E":
    print("Lopetit pelin!")
    print("Haluatko antaa palautetta? ")
    print("Syötä K jos haluat antaa palautetta tai syötä E jos et halua antaa palautetta.")
    user_help_answer = input("Haluatko antaa palautetta (K / E)? ").upper()
    if user_help_answer == "K":
        input("Anna palautetta: ")
        print()
        print("Kiitos palautteesta!")
    elif user_help_answer == "E":
        print("Peli ohi!")


















