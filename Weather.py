import requests

from datetime import datetime

api_key = '49664e3f02d7fccc81827c28993a31cc'
location= input("Enter the city name: ")

complete_api_link="https://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+api_key
api_link= requests.get(complete_api_link)
api_data= api_link.json()

temp_city= ((api_data[ 'main']['temp'] )-273.15)
weather_desc = api_data ['weather'][0]['description' ]
hmdt = api_data['main']['humidity']
wind_spd = api_data['wind' ]['speed']
date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")


print("____________________________________")
print ("Weather Stats for - {}  ||  {}". format(location.upper(), date_time))
print("____________________________________")

print ("Current temperature is  : {:.2f} deg C" .format(temp_city))
print ("Current weather desc : " , weather_desc)
print ("Current Humidity     : " , hmdt, "%")
print ("Current wind speed   : " ,  wind_spd, "kmph")


op = open('weather_report.txt', 'w')

op.write(str("City: "))
op.write(str(location))
op.write(str("  ;\n Date & Time: "))
op.write(str(date_time))
op.write(str("  ;\n Temprature in Celsius  :"))
op.write(str(temp_city))
op.write(str("  ;\n Weather  :"))
op.write(str(weather_desc))
op.write(str("  ;\n Humidity  :"))
op.write(str(hmdt))
op.write(str("  ;\n Wind Speed in kmph :"))
op.write(str(wind_spd))
op.write(str("\n____________________________________\n"))

op.close()
