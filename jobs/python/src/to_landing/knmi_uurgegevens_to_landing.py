from datetime import date, timedelta
from knmi import knmi
from src.generic.jdp import get_param_value


# TODO fetch the last run date
last_run_date = get_param_value('test')

print(last_run_date)

#knmi.load_knmi_to_landing('https://www.daggegevens.knmi.nl/klimatologie/uurgegevens', 'uurgegevens', date.today() - timedelta(days=1))
#knmi.load_knmi_to_landing('https://www.daggegevens.knmi.nl/klimatologie/uurgegevens', 'uurgegevens')