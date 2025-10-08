from flask import Flask, render_template
import random 
#pip install flask
app = Flask(__name__)
osebe = ["Adam Novák", "Ema Svobodová", "Jakub Dvořák", "Sofie Procházková", "Jan Kučera",
    "Anna Veselá", "Lukáš Horák", "Tereza Černá", "Matěj Král", "Natálie Fialová",
    "Filip Marek", "Adéla Pokorná", "Tomáš Jelínek", "Klára Holubová", "Petr Bláha",
    "Eliška Konečná", "David Malý", "Karolína Benešová", "Vojtěch Novotný", "Veronika Krejčí",
    "Marek Šimek", "Kristýna Hájková", "Ondřej Kolář", "Barbora Růžičková", "Daniel Němec",
    "Lucie Urbanová", "Michal Čech", "Marie Sedláčková", "Dominik Vacek", "Alžběta Pavlíková"]
kraji = [
    "Ljubljana", "Maribor", "Celje", "Kranj", "Velenje", "Novo Mesto", "Ptuj",
    "Trbovlje", "Nova Gorica", "Murska Sobota", "Kamnik", "Slovenj Gradec",
    "Škofja Loka", "Izola", "Piran", "Koper", "Postojna", "Sežana",
    "Žalec", "Radovljica", "Šentjur", "Kočevje", "Ravne na Koroškem",
    "Lendava", "Gornja Radgona", "Cerknica", "Vrhnika", "Tolmin",
    "Tržič", "Ilirska Bistrica"
]

@app.route("/")
def hello_world():
    oseba = random.choice(osebe)
    starost = random.randint(1,40)
    kraj = random.choice(kraji)
    return render_template("index.html", naslov = "Najboljša stran!",
                            osebe = oseba, starost = starost, kraji = kraj)
@app.route("/randomOseba")
def rndOseba():
    return "Page 2"


app.run(debug=True, port=5555)