from flask import Flask, request, render_template
from dotenv import load_dotenv
import os
import requests
import json

app = Flask(__name__)

load_dotenv()

@app.route('/',methods = ['GET','POST'])
def index():
    api_key = os.getenv("API_KEY")
    if request.method == 'POST':
        city = request.form.get('cityname').capitalize()

        if city.strip() != '':
            url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
            weather_response = requests.get(url)
            weather_data = weather_response.json()

            if 'message' not in weather_data:
                print("city found !!")

                main = weather_data['main']
                weath = weather_data['weather']
                wind = weather_data['wind']

                des = weath[0]['description']
                temp = main['temp']
                hum = main['humidity']
                wind_speed = wind['speed']

                return render_template('index.html',city = city, des = des, temp = temp, hum = hum, wind_speed = wind_speed)

            else:
                return render_template('index.html', not_found = 'City Not Found !!')
        else:
            return render_template('index.html', not_found = 'Please enter city name !!')


    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
