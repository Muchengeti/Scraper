import requests
from datetime import datetime, timedelta

def getMetrics():
    date = datetime.strftime(datetime.now() - timedelta(1), '%Y-%m-%d')
    print("retreiving metrics")

    API_KEY = 'FEBL88TRJ3PJCZVI'
    r = requests.get('https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=GLUU&interval=30min&apikey=' + API_KEY)
    if (r.status_code == 200):
        result = r.json()
        dataForAllDays = result['Time Series (Daily)']
        print(date)
        dataForSingleDate = dataForAllDays[date]
        print(dataForSingleDate['1. open'])
        print(dataForSingleDate['2. high'])
        print(dataForSingleDate['3. low'])
        print(dataForSingleDate['4. close'])
        print(dataForSingleDate['5. volume'])

def prev_weekday(adate):
    adate -= timedelta(days=1)
    while adate.weekday() > 4: # Mon-Fri are 0-4
        adate -= timedelta(days=1)
    return adate

def main():
    print("python main function")
    getMetrics()


if __name__ == '__main__':
    main()