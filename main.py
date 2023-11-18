from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.image import Image
import requests


imgs = Image(source='geography.gif')
bgimgs=Image(source='grey.jpg')

class MyLayout(Widget):
    img =imgs 
    bgimg =bgimgs
    def press(self):
        
        name = self.ids.name_input.text
        
        API_KEY = "48e0f28799caf6516459f702f31b95e3"
        BASE_URL = "https://api.openweathermap.org/data/2.5/weather/"
        city = name
        request_url = f"{BASE_URL}?appid={API_KEY}&q={city}"
        response = requests.get(request_url)
        
        if response.status_code == 200:
            data = response.json()
            weather = data['weather'][0]['description']
            icon = data['weather'][0]['icon']
            temperature = round(data["main"]["temp"] - 273.15, 2)
            feelslike = round(data["main"]["feels_like"] - 273.15, 2)
            windg = data ['wind']
            wind = windg['speed']
            print(data)
            #print("icon:",icon)
            #print("city: ", city)
            #print("weather : ",weather)
            #print("temperature :" ,temperature ,"celsius")
            #print("feelslike:" , feelslike)
            #print("wind:" , wind)
                 
            self.ids.name_label.text = name
            self.ids.weather_label.text = weather
            self.ids.temperature_label.text = str(temperature)+' c'
            self.ids.feelslike_label.text = str(feelslike)+" c"
            self.ids.wind_label.text = str(wind)+' km/h' 
                
            
            self.img.source=(icon + ".GIF")
            self.bgimg.source=(icon + ".jpg")    

        else:
            if name == "" :
                self.ids.name_label.text = "select a city"
                self.ids.weather_label.text = "select a city"
                self.ids.temperature_label.text = "select a city"
                self.ids.feelslike_label.text = "select a city"
                self.ids.wind_label.text = "select a city"
                #print("no city is selected")
            else  :
                self.ids.name_label.text = "chuld not faund " +name
                self.ids.weather_label.text = "chuld not faund " +name
                self.ids.temperature_label.text ="chuld not faund " +name
                self.ids.feelslike_label.text = "chuld not faund " +name
                self.ids.wind_label.text = "chuld not faund " +name
                #print("chuld not find city")
            
            

class MainApp(App):
    
    
    def build(self):
       return MyLayout()
    
        
if __name__ == '__main__':    
    MainApp().run()    