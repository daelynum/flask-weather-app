from flask import Flask, render_template, request
import requests

app = Flask(__name__)

URL = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid={}'
key = 'f5a91490cc7ce252a847cb3dbe1473f4'


@app.route('/', methods=['GET', 'POST'])
def get_weather():
    city = []
    if request.method == 'POST':
        city.append(request.form.get('city'))
    r = requests.get(URL.format(city[0], key)).json()

    icon = r['weather'][0]['icon']
    temperature = r['main']['temp']
    city = r['name']

    weather_data = {
        'city': city,
        'temperature': temperature,
        'icon': icon,
    }

    return render_template('weather.html', weather=weather_data)


if __name__ == "__main__":
    app.run(debug=True)