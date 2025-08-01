# ⛅ Weather App (Python + PyQt5)

This project is a **modern, GUI-based Weather App** built using **Python**, **PyQt5**, and the **OpenWeatherMap API**. It fetches live weather data for any city and displays the temperature, weather condition, and a weather emoji — all in a clean and stylish PyQt5 interface.

---

## 🌟 Features

- User-friendly PyQt5 GUI
- Fetches live weather data from OpenWeatherMap API
- Displays temperature, weather description, and matching emoji
- Handles API errors gracefully with custom messages
- Clean and readable code structure

---

## 🧰 Technologies Used

- Python 3.8+
- [PyQt5](https://pypi.org/project/PyQt5/)
- [requests](https://pypi.org/project/requests/)
- OpenWeatherMap API

---

## 📂 Folder Structure
```
WeatherApp/
├── WeatherApp.py # Main application script
├── weatherAppIcon.png # Icon shown on the app window
├── weather_screenshot.png # Screenshot of working application
└── README.md # Project documentation
```

---

## 🔑 How to Get an API Key

1. Go to [OpenWeatherMap](https://openweathermap.org/api)
2. Create a free account
3. Navigate to the API section and generate your API key
4. Replace the `api_key` value in the script with your key:
   ```python
   api_key = "your_api_key_here"
