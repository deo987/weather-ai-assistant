import requests

def get_weather(city: str):
    try:
        url = f"https://wttr.in/{city}?format=j1"
        res = requests.get(url, timeout=5)
        data = res.json()

        condition = data["current_condition"][0]
        temp = condition.get("temp_C", "N/A")
        desc = condition["weatherDesc"][0]["value"]

        return f"It’s {temp}°C in {city}. Weather condition: {desc}."

    except Exception as e:
        return f"Sorry, I couldn't fetch the weather for {city}."
