import pandas as pd
import datetime
import pandas_datareader.data as web
from pandas import Series, DataFrame
import matplotlib.pyplot as plt
from matplotlib import style
import matplotlib as mpl


def getMetrics():
    start = datetime.datetime(2019, 1, 1)
    end = datetime.datetime(2020, 1, 25)

    df = web.DataReader("GLUU", 'yahoo', start, end)
    print("GLUU stock data\n")
    print(df)
    df.tail()

    close_px = df['Adj Close']
    mavg = close_px.rolling(window=100).mean()
    print("rolling average\n")
    print(mavg)

    # Adjusting the size of matplotlib
    mpl.rc('figure', figsize=(8, 7))
    mpl.__version__

    # Adjusting the style of matplotlib
    style.use('ggplot')

    close_px.plot(label='GLUU')
    mavg.plot(label='100 Day Moving Avg')
    plt.legend()
    plt.show()
    

def main():
    print("python main function")
    getMetrics()


if __name__ == '__main__':
    main()