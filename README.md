# Openweathermap_API_Data

# Python file converts Openweathermap API JSON to python variables.

Add your API Key to the python file from https://openweathermap.org/appid
Enter the latitude and longitude of the desired weather forecast.
Uncomment either imperial or metric units.
Run script.

# Openweathermap API json output as variables

The script will list all available data points available from the Openweathermap API with a python variable name.  

See https://openweathermap.org/api/hourly-forecast for explanation of data.
Openweathermap provides a forecast every three hours over the next five days.
The forecasts are numbered from 0 to 39, you may choose which forecast time period.
Set the item variable to the desired time period for forecast, from 0 to 39

# Five Day Daily Forecast

The script will also print a five day weather forecast for the entered latitude and longitude, using some of the variables printed above.
Note that the min and max temperatures apply only to the 3 hour timeframe of the forecast, not the entire day.

# Print Full length JSON file

To see a full length json printout of the Openweathermap API resource, uncomment:
#pprint(forecast_json)
