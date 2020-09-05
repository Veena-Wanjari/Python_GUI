import tkinter as tk
import requests

HEIGHT = 500
WIDTH = 600

#8cd3eca5cc116d55c940f5fb45bb37a5
#api.openweathermap.org/data/2.5/weather?q={city name}&appid={your api key}
def test_function(entry):
    print("This is the entry:", entry)
    
def format_response(weather):
    try: 
    
        name = weather['name']
        desc = weather['weather'][0]['description']
        temp = weather['main']['temp']
    
        #final_str = 'City: %s \n Conditions: %s \n Temperature(F): %s'%(name, disc, temp)
        final_str = name + " " + desc + " " + str(temp)
    except:
        final_str = "There is a problem in retrieving that information."

    return final_str
    
def get_weather(city):
    weather_key = '8cd3eca5cc116d55c940f5fb45bb37a5'
    url = 'https://api.openweathermap.org/data/2.5/weather'
    params = {'APPID': weather_key, 'q' : city, 'units' : 'imperial'}
    response = requests.get(url, params = params)
    weather = response.json()
    
    label['text'] = format_response(weather)
       
    
root = tk.Tk()

canvas = tk.Canvas(root, height = HEIGHT, width = WIDTH)
canvas.pack()

frame = tk.Frame(root, bg = '#80c1ff', bd = 5)
frame.place(relx = 0.5, rely = 0.1, relwidth = 0.75, relheight = 0.1, anchor = 'n')

entry = tk.Entry(frame, font = 40)
entry.place(relwidth = 0.65, relheight = 1)

button = tk.Button(frame, text = "Get Weather", font = 40, command = lambda: get_weather(entry.get()))
button.place(relx = 0.7,relwidth = 0.3, relheight = 1)

lower_frame = tk.Frame(root, bg = '#80c1ff', bd = 10)
lower_frame.place(relx = 0.5, rely = 0.25, relwidth = 0.75, relheight = 0.6, anchor = 'n')


label = tk.Label(lower_frame, font = 40)
label.place(relwidth = 1, relheight = 1)
root.mainloop()
