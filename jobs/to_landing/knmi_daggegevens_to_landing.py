from datetime import date, timedelta
from knmi import knmi


# TODO fetch the last run date

knmi.load_knmi_to_landing('https://www.daggegevens.knmi.nl/klimatologie/daggegevens', 'daggegevens', date.today() - timedelta(days=1))