import requests
from datetime import datetime, timedelta

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
    r = requests.get('https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=MSFT&interval=30min&apikey=' + API_KEY)
    if (r.status_code == 200):
        result = r.json()
        dataForAllDays = result['Time Series (Daily)']
        count = 5
        while count >= 0:
            date = prev_weekday(date)
            date_string = datetime.strftime(date, '%Y-%m-%d')
            print(date_string)
            dataForSingleDate = dataForAllDays[date_string]
            print(dataForSingleDate['1. open'])
            print(dataForSingleDate['2. high'])
            print(dataForSingleDate['3. low'])
            print(dataForSingleDate['4. close'])
            print(dataForSingleDate['5. volume'])
            count -= 1
    print("retreived metrics")

def prev_weekday(adate):
    adate -= timedelta(days=1)
    while adate.weekday() > 4: # Mon-Fri are 0-4
        adate -= timedelta(days=1)
    return adate

def main():
    print("python main function")
    getMetrics()
    getMetrics5Day()


if __name__ == '__main__':
    main()