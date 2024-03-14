n = int(input())

class WeatherInfo :
    def __init__(self, date, day, weather) :
        self.day = day
        self.date = date
        self.weather = weather

inputs = [input().split() for _ in range(n)]
weathers = [WeatherInfo(a, b, c) for a, b, c in inputs]

idx = -1
for i, w in enumerate(weathers) :
    if w.weather == "Rain" :
        if idx == -1 :
            idx = i
        else :
            if w.date < weathers[idx].date :
                idx = i


print(f"{weathers[idx].date} {weathers[idx].day} {weathers[idx].weather}")