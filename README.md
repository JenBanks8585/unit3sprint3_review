# unit3sprint3_review
Review material for Unit3 Sprint3

We will retrieve weather information from https://openweathermap.org/.
1. Go to the Open Weather Map website and register (for free):
2. Once logged in, go to https://home.openweathermap.org/api_keys 
     in order to copy your API key (edited)
3. There a number of available APIs there, but we will just concentrate
    ONE CALL API
4. Minimum installations:  `pip install Flask Flask-SQLAlchemy requests`
5. You should create your own `.py` file to house your solution. 
6. A sample implementation is in `weather.py`. It is preferable that you do not access it until you create your own solution.
7. Choose an API call that will only require for `lat`, `lon` and `api key`

Location to search:
Use the following variables to search
* lat = "48.208176"
* lon = "16.373819"



Tasks:
 * A. Create an endpoint (main route) that shows the information provided (if in dictionary, this means the keys)
  Note: Answer should be something like this: 
  `['dt', 'sunrise', 'sunset', 'temp', 'feels_like', 'pressure', 
  'humidity', 'dew_point', 'wind_speed', 'wind_deg', 'weather', 'clouds', 'pop', 'uvi']`
 * B. Create another endpoint ('/results') that shows the first 3 results of "DAILY"
 * C. Create a database that stores the following information
     * a. id
     * b. clouds 
     * c. humidity
     * d. pressure
 * D. Create a query from database at this endpoint ('/query') that returns the data from the database.

Thanks to the following participants and contributors: Elizabeth, Victoria, Justin, Rassamy, Micah, Drew, Henry, Ik, Jacob, Antony, Nathan, Marcos
