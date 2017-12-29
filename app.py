from flask import Flask, render_template, request, redirect, url_for
from stock import Stock
# user input
from flask_wtf import Form
from wtforms.fields import RadioField, StringField, SubmitField, SelectField
from wtforms.validators import Required
from bokeh.embed import components


app = Flask(__name__)
stock = Stock()

@app.route('/')
def index():
  return render_template('index.html',
  tickerlist = [{'ticker' : ticker} for ticker in stock.tickers])

@app.route('/display_ticker/', methods=['GET', 'POST'])
def display_ticker():
    ticker = request.form.get('comp_select')
    feature = request.form.get('features')
    # return(str(select)) # just to see what select is
    plot = stock.create_stock_plot(ticker, feature)
    script, div = components(plot)
    return render_template("display_ticker.html", ticker=ticker,
    title = stock.title, nasdaq = stock.nasdaq,
    the_div=div, the_script=script)

@app.errorhandler(404)
def page_not_found(error):
    return 'This page does not exist', 404

if __name__ == '__main__':
  app.run(port=33507)
