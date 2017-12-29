# pull data
import requests
import simplejson as json

#data analysis
import pandas as pd
import datetime
import time
from math import pi

#plot
from bokeh.models import ColumnDataSource
from bokeh.plotting import figure, show, output_file
from bokeh.models import DatetimeTickFormatter

class Stock:
    def __init__(self):
        self.df = pd.DataFrame()
        self.tickers = []
        self.nasdaq = ''
        self.set_df()
        self.set_tickers()

    def set_df(self):
        r = requests.get('https://www.quandl.com/api/v3/datatables/WIKI/PRICES.json?api_key=Tw2yYK7DQ7hzMWvQqVYi', auth=('user', 'pass'))
        column_names = [s["name"] for s in r.json()['datatable']["columns"]]
        values = r.json()['datatable']['data']
        df = pd.DataFrame(values, columns = column_names)
        df["date"] = pd.to_datetime(df["date"])
        self.df = df

    def set_tickers(self):
        self.tickers = list (self.df['ticker'].unique())

    def create_stock_plot(self, ticker, feature):
        # source = ColumnDataSource(self.df[self.df['ticker']== ticker])
        self.nasdaq = "http://www.nasdaq.com/symbol/" + ticker.lower() + "/real-time"
        t = 'Regular' if feature == '' else 'Adjusted'
        self.title = 'Quandl WIKI ' + t +' Stock Prices: ' + ticker

        p = figure(plot_width=800, plot_height=400,
                x_axis_label='date', y_axis_label='price', x_axis_type="datetime")

        df_plot = self.df[self.df['ticker']== ticker]
        df_plot = df_plot.sort_values(by="date",ascending=True).set_index("date").last("30D")
        df_plot = df_plot.reset_index()

        # p.title.text = 'Quandl WIKI ' + t +' Stock Prices: ' + ticker
        # p.line('date', feature + 'open', source = source, color='navy', alpha=0.5, legend = 'open')
        # p.line('date', feature + 'close', source = source, color='red', alpha=0.5, legend = 'close')
        # p.line(df_plot['date'], df_plot[feature + 'open'],  color='navy', alpha=0.5, legend = 'open')
        p.line(df_plot['date'], df_plot[feature + 'close'], color='red', alpha=0.5, legend = 'close')

        p.legend.location = "top_right"
        p.legend.click_policy="hide"
        p.xaxis.formatter=DatetimeTickFormatter(years=["%B %Y"],)
        p.xaxis.major_label_orientation = pi/4
        return p
