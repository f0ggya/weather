import requests
from datetime import datetime, timedelta
from flask import Flask, render_template, request 

app = Flask(__name__)
def get_direction(wind_deg):
    if wind_deg < 22.5:
        return 'Северный' 
    elif wind_deg < 67.5:
        return 'Северо-восточный'
    elif wind_deg < 112.5:
        return 'Восточный'
    elif wind_deg < 157.5:
        return 'Юго-восточный'
    elif wind_deg < 202.5:
        return 'Южный'
    elif wind_deg < 247.5:
        return 'Юго-западный'
    elif wind_deg < 292.5:
        return 'Западный'
    elif wind_deg < 337.5:
        return 'Cеверо-западный'
    else:
        return 'Cеверный'

@app.route('/', methods=['GET', 'POST'])
def main():
    if request.method == 'POST':
        cityName = request.form['city_name']
        lang = request.form['lang']
        openWeather = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={cityName}&lang={lang}&appid=4fe859a6005c2ef9e718091ffd266358&units=metric").json()
        print(openWeather)
        city = openWeather['name']
        weather = openWeather['weather'][0]['description']
        temp = round(openWeather['main']['temp'])
        wind_speed = round(openWeather['wind']['speed'])
        wind_deg = get_direction(openWeather['wind']['deg'])
        sunrise = datetime(1970,1,1) + timedelta(seconds=openWeather['sys']['sunrise']) + timedelta(seconds=openWeather['timezone'])
        sunset = datetime(1970,1,1) + timedelta(seconds=openWeather['sys']['sunset']) + timedelta(seconds=openWeather['timezone'])
        pressure = openWeather['main']['pressure']
        data = {'weather': weather, 'temp': temp, 'wind_speed': wind_speed,'wind_deg': wind_deg,'sunrise': sunrise,'sunset': sunset,'pressure': pressure, 'city': city}
        return render_template('home.html', data=data)
    else:
        return render_template('input.html')    



if __name__ == '__main__':
    app.run()


#город и страна запроса