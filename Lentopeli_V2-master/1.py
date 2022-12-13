#  import mysql.connector
from flask import Flask, render_template, url_for, request, jsonify, g
from flask_mysqldb import MySQL
import random
import geopy.distance
import requests

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'benjamn'
app.config['MYSQL_PASSWORD'] = 'Metrolippu23'
app.config['MYSQL_DB'] = 'flight_game'

mysql = MySQL(app)




@app.route("/")
def home():
    return render_template("welcome.html")  # palauttaa welcome.html


@app.route("/play")
def play():
    cur1 = mysql.connection.cursor()
    cur1.execute("SELECT name, latitude_deg, longitude_deg FROM airport WHERE iso_country = 'FI'") # Lähtökentän tietojen keräys db:stä
    data1 = cur1.fetchall()
    starting_airport = random.choice(data1)
    real_data3 = starting_airport[1]  # Airport latitude
    real_data4 = starting_airport[2]  # Airport longitude
    real_data1 = starting_airport[0]  # Airport nimi
    coord1 = starting_airport[1:3]  # lon and lat
    real_data1 = real_data1.strip("()")
    g.starting_airport = real_data1
    cur2 = mysql.connection.cursor()
    cur2.execute("SELECT name, latitude_deg, longitude_deg FROM airport") # Kohde kentän tietojen keräys db:stä
    data2 = cur2.fetchall()
    destination_airport = random.choice(data2)
    real_data5 = destination_airport[1]  # Airport latitude
    real_data6 = destination_airport[2]  # Airport longitude
    real_data2 = destination_airport[0]  # Airport nimi
    coord2 = destination_airport[1:3]  #lon and lat
    real_data2 = real_data2.strip("()")
    g.destination_airport = real_data2
    cur2 = mysql.connection.cursor()
    real_data7 = geopy.distance.geodesic(coord1, coord2).km   # Lähtö kentän ja kohde kentän etäisyys
    real_data7 = round(real_data7)
    cur3 = mysql.connection.cursor()
    cur3.execute("SELECT points, co2_consumed FROM players")  # KESKEN. Pelaajan pisteiden ja co2 päästöjen haku
    data3 = cur3.fetchall()
    points = data3[0]
    co2_c = data3[0]
    # point_multiplier = 0.15
    # result = list(map(lambda y: y * point_multiplier, co2_c[0]))
    return render_template("play.html", data1=real_data1, data2=real_data2, starting_airport_lat=real_data3, starting_airport_lon=real_data4, destination_airport_lat=real_data5, destination_airport_lon=real_data6, distance_between=real_data7, points=points, co2_consumed=co2_c)


@app.route("/stop")
def stop():
    return render_template("stop.html")  # Palauttaa stop.html


@app.route("/info")
def info():
    return render_template("about.html")  # Palauttaa about.html


@app.route("/game")
def homepage():
    return render_template("home.html")  # Palauttaa home.html


"""@app.route("/weather")   
def weather():
    cur3 = mysql.connection.cursor()
    cur3.execute(f"SELECT municipality FROM airport  WHERE name = '{g.real_data1}'")
    data3 = cur3.fetchall()
    municipality = data3[0][0]
    return jsonify({'municipality': municipality})"""   # KESKEN


if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000, debug=True)
