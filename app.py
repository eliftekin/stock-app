from flask import Flask, render_template, request, redirect, url_for
from stock import Stock

# user input
from wtforms.fields import RadioField, StringField, SubmitField, SelectField
from wtforms.validators import Required
from bokeh.embed import components

app = Flask(__name__)
stock = Stock()

@app.route('/')
def index():
    return render_template('index.html')
  # return render_template('index.html',
  # tickerlist = [{'ticker' : ticker} for ticker in stock.tickers])

@app.route('/display_ticker/', methods=['GET', 'POST'])
def display_ticker():
    ticker = request.form.get('ticker')
    features = request.form.getlist('features')
    if ticker == None and stock.ticker == None:
        return render_template("error_message.html", msg = "Error: Please enter valid Ticker Symbol")

    if not ticker == None:
        stock.set_ticker(ticker)
        stock.set_features(features)
        stock.get_request()

    if stock.error:
        return render_template("error_message.html", msg = "Error: Please enter valid Ticker Symbol")
    else:
        plot = stock.create_stock_plot()
        script, div = components(plot)
        title = "Error: Please select price category" if stock.features == [] else stock.title
        return render_template("display_ticker.html", ticker=ticker,
                                title = title, nasdaq = stock.nasdaq,
                                the_div=div, the_script=script)

@app.errorhandler(404)
def page_not_found(error):
    return 'This page does not exist', 404

if __name__ == '__main__':
  app.run(port=33507)
