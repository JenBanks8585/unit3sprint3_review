# unit3sprint3_review
Review material for Unit3 Sprint3

We will retrieve weather information from https://openweathermap.org/.
1. Go to the Open Weather Map website and register (for free):
2. Once logged in, go to https://home.openweathermap.org/api_keys 
     in order to copy your API key (edited)
3. There a number of available APIs there, but we will just concentrate
    ONE CALL API
4. Choose an API call that will only require for `lat`, `lon` and `api key`

Tasks:
 * A. Create an endpoint (main route) that shows the information provided (if in dictionary, this means the keys)
  Note: Answer should be something like this 
  ['dt', 'sunrise', 'sunset', 'temp', 'feels_like', 'pressure', 
  'humidity', 'dew_point', 'wind_speed', 'wind_deg', 'weather', 'clouds', 'pop', 'uvi']
 * B. Create another endpoint ('/results') that shows the first 3 results of "DAILY"
 * C. Create a database that stores the following information
     * a. id
     * b. clouds 
     * c. humidity
     * d. pressure
 * D. Create a query from database at this endpoint ('/query')
