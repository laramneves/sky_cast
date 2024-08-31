from django.shortcuts import render #the function render will render a template and return an http response

# Create your views here.

import urllib.request #to open and read urls
import json



def page(request):
    if request.method == 'POST':
        city = request.POST['city'] #dicitionary like object to hold the data
        source = urllib.request.urlopen('https://api.openweathermap.org/data/2.5/weather?q=' + city + '&units=metric&appid=8d8924bd72c23b76a453a34fcecdb807').read()
        list_data = json.loads(source) #this will hold all the data that we are requesting
       
        #this will render everthing in index.html
        data = {
            "cordinate" : str(list_data['coord']['lon']) + ' ' + str(list_data['coord']['lat']),
            "country_code" : str(list_data['sys']['country']),
            "temp" : str(list_data['main']['temp']) + ' ºC',
            "pressure" : str(list_data['main']['pressure']),
            "humidity" : str(list_data['main']['humidity']),
            "main" : str(list_data['weather'][0]['main']), #the zero is to acess the first element in the list
            "description" : str(list_data['weather'][0] ['description']), #the last 3 items are inside the weather
            "icon" : list_data['weather'][0]['icon'],
        }
        print(data)

    else:
        data = {} #if the user hasn't submitted the form yet, there will be no weather data to display.

    return render(request, "main/index.html", data) #this will render everthing in index.html located in templates


        
