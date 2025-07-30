import sys
import requests
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QPushButton,
                             QLineEdit, QVBoxLayout)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon

class WeatherApp(QWidget):
    def __init__(self):
        super().__init__()
        self.cityLabel = QLabel("Enter city name: ", self)
        self.cityInput = QLineEdit(self)
        self.getWeatherButton = QPushButton("Get Weather", self)
        self.tempLabel = QLabel(self)
        self.emojiLabel = QLabel(self)
        self.descriptionLabel = QLabel(self)
        self.setWindowIcon(QIcon("weatherAppIcon.png"))

        self.initUI()

    def initUI(self):
        self.setWindowTitle("Weather App")

        vbox = QVBoxLayout()

        vbox.addWidget(self.cityLabel)
        vbox.addWidget(self.cityInput)
        vbox.addWidget(self.getWeatherButton)
        vbox.addWidget(self.tempLabel)
        vbox.addWidget(self.emojiLabel)
        vbox.addWidget(self.descriptionLabel)

        self.setLayout(vbox)

        self.cityLabel.setAlignment(Qt.AlignCenter)
        self.cityInput.setAlignment(Qt.AlignCenter)
        self.tempLabel.setAlignment(Qt.AlignCenter)
        self.emojiLabel.setAlignment(Qt.AlignCenter)
        self.descriptionLabel.setAlignment(Qt.AlignCenter)

        self.cityLabel.setObjectName("cityLabel")
        self.cityInput.setObjectName("cityInput")
        self.getWeatherButton.setObjectName("getWeatherButton")
        self.tempLabel.setObjectName("tempLabel")
        self.emojiLabel.setObjectName("emojiLabel")
        self.descriptionLabel.setObjectName("descriptionLabel")

        self.setStyleSheet("""
            QLabel, QPushButton, QLineEdit{
                font-family: Calibri;
                font-size: 40px;
            }
            QLabel#cityLabel{
                font-style: Italic;
            }
            QPushButton#getWeatherButton{
                font-size: 30px;
                font-weight: bold;
            }
            QLabel#emojiLabel{
                font-size: 100px;
                font-family: Segoe UI emoji;
            }
        """)

        self.getWeatherButton.clicked.connect(self.getWeather)
        self.cityInput.returnPressed.connect(self.getWeather)

    def getWeather(self):
        api_key = "acf72463527fff632c8b4bdb9a2db0e1"
        city = self.cityInput.text()
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

        try:
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()

            if data["cod"] == 200:
                self.displayWeather(data)

        except requests.exceptions.HTTPError as http_error:
            match response.status_code:
                case 400:
                    self.displayError("Bad Request:\nPlease check your input")
                case 401:
                    self.displayError("Unauthorized:\nInvalid API key")
                case 403:
                    self.displayError("Forbidden:\nAccess denied")
                case 404:
                    self.displayError("Not Found:\nCity not found")
                case 500:
                    self.displayError("Server Error:\nPlease try again later")
                case 502:
                    self.displayError("Bad Gateway:\nInvalid response from the server")
                case 503:
                    self.displayError("Server Unavailable:\nServer is down")
                case 504:
                    self.displayError("Gateway Timeout:\nNo response from the server")
                case _:
                    self.displayError(f"HTTP error occurred:\n{http_error}")

        except requests.exceptions.ConnectionError:
            self.displayError("Connection Error:\nCheck your internet connection.")

        except requests.exceptions.RequestException as req_error:
            self.displayError(f"Request Error: {req_error}")

    def displayError(self, message):
        self.tempLabel.setStyleSheet("font-size: 30px;")
        self.tempLabel.setText(message)
        self.emojiLabel.clear()
        self.descriptionLabel.clear()

    def displayWeather(self, data):
        self.tempLabel.setStyleSheet("font-size: 75px;")
        temp_c = data["main"]["temp"]
        weather_description = data["weather"][0]["description"]
        weather_id = data["weather"][0]["id"]

        self.tempLabel.setText(f"{temp_c:.1f}°C")
        self.emojiLabel.setText(self.getEmoji(weather_id))
        self.descriptionLabel.setText(weather_description)

    @staticmethod
    def getEmoji(weather_id):
        if 200 <= weather_id <= 232:
            return "⛈️"
        elif 300 <= weather_id <= 321:
            return "🌦️"
        elif 500 <= weather_id <= 531:
            return "🌧️"
        elif 600 <= weather_id <= 622:
            return "❄️"
        elif 701 <= weather_id <= 741:
            return "🌫️"
        elif weather_id == 762:
            return "🌋"
        elif weather_id == 771:
            return "💨"
        elif weather_id == 781:
            return "🌪️"
        elif weather_id == 800:
            return "☀️"
        elif 801 <= weather_id <= 804:
            return "☁️"
        else:
            return ""

def main():
    app = QApplication(sys.argv)
    weather_app = WeatherApp()
    weather_app.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()