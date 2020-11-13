import requests
from flask import Flask 
from flask_sqlalchemy import SQLAlchemy 
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///db.sqlite3"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 
DB = SQLAlchemy(app)
lat = "48.208176"
lon = "16.373819"
API_key = "69dee9b401f7bf1265fdc42ab14c4460"
URL = f"https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lon}&appid={API_key}"
request = requests.get(URL)
data = request.json()
@app.route('/')
def root():
    return str(data.keys())
@app.route('/results')
def results():
    return str(data["daily"][:3])
@app.route('/weather')
def weather():
    DB.drop_all()
    DB.create_all()
    weathers = []
    cloud_data = [data["daily"][i]["clouds"] for i in range(len(data["daily"]))]
    humid_data = [data["daily"][i]["humidity"] for i in range(len(data["daily"]))]
    press_data = [data["daily"][i]["pressure"] for i in range(len(data["daily"]))]
    for i in range(len(cloud_data)):
        weather = Weather()
        weather.id = i
        weather.clouds = cloud_data[i]
        weather.humidity = humid_data[i]
        weather.pressure = press_data[i]
        DB.session.add(weather)
        weathers.append(weather)
    DB.session.commit()
    all_weather = Weather.query.all()
    return str(all_weather)
# Create database
class Weather(DB.Model):
    id = DB.Column(DB.BigInteger, primary_key=True)
    clouds = DB.Column(DB.BigInteger, nullable=False)
    humidity = DB.Column(DB.BigInteger, nullable=False)
    pressure = DB.Column(DB.BigInteger, nullable=False)
    def __repr__(self):
        dictionary = {"id": self.id, 
                      "clouds": self.clouds,
                      "humidity" : self.humidity,
                      "pressure" : self.pressure}
        return str(dictionary)
