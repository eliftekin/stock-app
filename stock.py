# pull data
import requests
import simplejson as json

#data analysis
import datetime as dt
import pandas as pd

#plot
from bokeh.models import ColumnDataSource, Range1d, Label
from bokeh.plotting import figure, show, output_file
from bokeh.models import DatetimeTickFormatter, DatePicker

class Stock:
    def __init__(self):
        self.df = pd.DataFrame()
        self.ticker = None
        self.error = False
        self.features = []
        self.nasdaq = ""
        self.title = ""

    def set_ticker(self, ticker):
        self.ticker =ticker
        self.nasdaq = "http://www.nasdaq.com/symbol/" + self.ticker.lower() + "/real-time"

    def set_features(self, features):
        self.features = features

    def get_request(self):
        '''Pull one-month data from API of self.ticker and convert to pandas df'''

        today = dt.date.strftime(dt.date.today(), format = "%Y-%m-%d")
        one_month_ago = dt.date.strftime(dt.date.today() - dt.timedelta(days=30), format = "%Y-%m-%d")
        api_link_day_info = "start_date=" + one_month_ago + "&" + "end_date=" + today
        api_link = 'https://www.quandl.com/api/v3/datasets/WIKI/' + self.ticker +'.json?&'+ api_link_day_info + '&api_key=Tw2yYK7DQ7hzMWvQqVYi'
        r = requests.get(api_link)
        self.error = not r.ok

        if r.ok: # check if correct ticker symbol is given by user
            column_names = r.json()['dataset']["column_names"]
            values = r.json()['dataset']['data']
            df = pd.DataFrame(values, columns=column_names)
            df["Date"] = pd.to_datetime(df["Date"])
            self.df = df

    def create_stock_plot(self):
        self.title = 'Quandl WIKI '+ str(self.df["Date"].min())[0:4] +' Stock Prices: ' + self.ticker
        colors = ['red' if feature == 'Open' else 'navy' for feature in self.features]
        p = figure(plot_width=800, plot_height=400,
                x_axis_label="Date", y_axis_label='Price', x_axis_type="datetime")

        for feature, color in zip(self.features, colors):
            p.circle(self.df["Date"], self.df[feature], size=2, color=color, alpha=0.8)
            p.line(self.df["Date"], self.df[feature], color=color, line_width=2, alpha=0.5, legend = feature)

        # set plot options
        p.legend.location = "top_right"
        p.legend.click_policy="hide"
        p.xaxis.formatter=DatetimeTickFormatter(years=["%B %Y"])
        return p
