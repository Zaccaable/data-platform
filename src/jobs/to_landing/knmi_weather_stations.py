from datetime import date, timedelta
from knmi import knmi

# Weather station aare in the csv header. we just need to retrieve something to get the header data.
knmi.load_knmi_to_landing('https://www.daggegevens.knmi.nl/klimatologie/daggegevens', 'weather_stations', date.today() - timedelta(days=1))