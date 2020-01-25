import requests
from datetime import datetime, timedelta
import datetime as dt


def getMetrics():
    date = datetime.now() - timedelta(1)
    date_string = datetime.strftime(date, '%Y-%m-%d')
    print("retreiving metrics")

    API_KEY = 'FEBL88TRJ3PJCZVI'
    r = requests.get('https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=GLUU&interval=30min&apikey=' + API_KEY)
    if (r.status_code == 200):
        result = r.json()
        dataForAllDays = result['Time Series (Daily)']
        print(date)
        dataForSingleDate = dataForAllDays[date_string]
        print(dataForSingleDate['1. open'])
        print(dataForSingleDate['2. high'])
        print(dataForSingleDate['3. low'])
        print(dataForSingleDate['4. close'])
        print(dataForSingleDate['5. volume'])

        print("retreived metrics")

def getMetrics5Day():
    date = datetime.now() - timedelta(1)
    date_string = datetime.strftime(date, '%Y-%m-%d')
    print("retreiving 5 day metrics")

    API_KEY = 'FEBL88TRJ3PJCZVI'
    r = requests.get('https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=GLUU&interval=30min&apikey=' + API_KEY)
    if (r.status_code == 200):
        result = r.json()
        dataForAllDays = result['Time Series (Daily)']
        count = 5
        prev_date = date
        while count >= 0:
            prev_date = prev_weekday(prev_date)
            try:
                prev_date_string = datetime.strftime(prev_date, '%Y-%m-%d')
                print(prev_date_string)
                dataForSingleDate = dataForAllDays[prev_date_string]
                print(dataForSingleDate['1. open'])
                print(dataForSingleDate['2. high'])
                print(dataForSingleDate['3. low'])
                print(dataForSingleDate['4. close'])
                print(dataForSingleDate['5. volume'])
            except KeyError:
                print("An exception occurred, No metrics for this day")
            count -= 1
    print("retreived metrics")

def prev_weekday(adate):
    adate -= timedelta(days=1)
    while adate.weekday() > 4: # Mon-Fri are 0-4
        print("previous day loop")
        print(adate.weekday())
        adate -= timedelta(days=1)
    print("previous day")
    print(adate.weekday())
    return adate

def main():
    print("python main function")
    getMetrics()
    getMetrics5Day()


if __name__ == '__main__':
    main()