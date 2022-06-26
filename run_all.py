from all_time import AllTimeScraper
from daily import DailyScraper
from seven_days import SevenDaysScraper
from thirty_days import ThirtyDaysScraper
import time
import schedule


def run_app():

    my_all_time = AllTimeScraper()
    my_all_time.run_all()
    time.sleep(1)
    mydaily = DailyScraper()
    mydaily.run_all()
    time.sleep(1)
    mysevendays = SevenDaysScraper()
    mysevendays.run_all()
    time.sleep(1)
    my_thirty_days = ThirtyDaysScraper()
    my_thirty_days.run_all()

if __name__ == '__main__':

    run_app()
    schedule.every(24).hours.do(run_app)
